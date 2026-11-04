"""
Módulo de integração com a API do GitHub via PyGithub e extração de metadados e horas das issues.
"""

from datetime import datetime
import json
import os
import re
import sys

from github import Auth, Github
from github.GithubException import GithubException

from .config import (
    CACHE_FILE,
    REPO_FULL_NAME,
    format_date_display,
    get_github_token,
    normalize_user,
    parse_closed_datetime,
    parse_date_string,
)


def _get_github_instance(token: str | None = None) -> Github:
    """Inicializa a instância do PyGithub com token de autenticação ou anônima."""
    if token:
        return Github(auth=Auth.Token(token))
    return Github()


def _extract_contribution_table(body: str, issue_number: str) -> list[dict]:
    """
    Extrai os registros da '### Tabela de Contribuição' presente no corpo da issue.
    Formato esperado:
        | Usuário | Data | Horas Trabalhadas |
        | @CamilaSilvaC | 20/10/2026 | 0.5 |
    """
    registros = []
    if not body:
        return registros

    lines = body.splitlines()
    in_table = False

    for line in lines:
        line_clean = line.strip()
        # Identifica o cabeçalho da tabela de contribuição
        if "tabela de contribui" in line_clean.lower():
            in_table = True
            continue

        if in_table:
            # Novo cabeçalho de seção encerra a tabela
            if line_clean.startswith("##") and not line_clean.startswith("###"):
                in_table = False
                continue

            if line_clean.startswith("|"):
                parts = [p.strip() for p in line_clean.strip("|").split("|")]
                if len(parts) >= 3:
                    u_raw, d_raw, h_raw = parts[0], parts[1], parts[2]
                    # Pula linha de cabeçalho ou separador da tabela markdown
                    if "usuário" in u_raw.lower() or "usuario" in u_raw.lower() or "---" in u_raw:
                        continue

                    membro_chave = normalize_user(u_raw)
                    dt_obj = parse_date_string(d_raw)
                    data_iso = dt_obj.strftime("%Y-%m-%d") if dt_obj else d_raw.strip()

                    try:
                        horas_val = float(h_raw.lower().replace("h", "").replace(",", ".").strip())
                    except ValueError:
                        continue

                    registros.append({
                        "membro": membro_chave,
                        "usuario_raw": u_raw,
                        "data": data_iso,
                        "horas": horas_val,
                        "issue": issue_number,
                    })
            elif line_clean and (line_clean.startswith("#") or line_clean.startswith("- [ ]") or line_clean.startswith("- [x]")):
                in_table = False

    return registros


def _parse_issue_payload(item: dict) -> dict:
    """Extrai campos estruturados de um dicionário serializado de issue."""
    num = str(item.get("number"))
    body = item.get("body") or ""

    # Extração de estimativa original (He)
    est_match = re.search(
        r"(?:estimativa(?:\s+original)?|horas?\s+estimadas?)\s*[*_]*\s*(?:\([^)]*\)\s*)?[:\|]\s*[*_]*\s*([0-9]+(?:[\.,][0-9]+)?)",
        body,
        re.IGNORECASE,
    )
    estimativa = float(est_match.group(1).replace(",", ".")) if est_match else None

    # Extração de janela original (Ap / Acp)
    jan_match = re.search(
        r"(?:janela(?:\s*(?:prevista|original))?|entrega(?:\s*prevista)?)\s*[*_]*\s*[:\|]\s*[*_]*\s*([0-9]{1,2}/[0-9]{1,2}(?:/[0-9]{2,4})?|[0-9]{4}-[0-9]{2}-[0-9]{2})",
        body,
        re.IGNORECASE,
    )
    janela_raw = jan_match.group(1).strip() if jan_match else None
    janela_date = parse_date_string(janela_raw)

    # Milestone e labels
    ms = item.get("milestone")
    ms_title = ms.get("title") if isinstance(ms, dict) else (getattr(ms, "title", None) if ms else None)
    raw_labels = item.get("labels", [])
    labels = [
        lbl.get("name") if isinstance(lbl, dict) else getattr(lbl, "name", str(lbl))
        for lbl in raw_labels
    ]
    labels_lower = [lbl.lower() for lbl in labels]

    if not ms_title:
        if "fase-1" in labels_lower or "fase 1" in labels_lower:
            ms_title = "Fase 1"
        elif "fase-2" in labels_lower or "fase 2" in labels_lower:
            ms_title = "Fase 2"
        elif "fase-3" in labels_lower or "fase 3" in labels_lower:
            ms_title = "Fase 3"
        elif "fase-4" in labels_lower or "fase 4" in labels_lower:
            ms_title = "Fase 4"
        else:
            ms_title = "Outras atividades"

    closed_at = item.get("closed_at")
    closed_date = parse_closed_datetime(closed_at)

    # Critérios associados (ex: F1-C1, F2-C4)
    criterios = sorted(list(set(re.findall(r"\bF[1-4]-C\d+\b", body, re.IGNORECASE))))

    # Detecção de Retrabalho (DP1)
    tem_label_correcao = any(
        lbl in ["correcao", "correção", "retrabalho", "bug", "fix"] for lbl in labels_lower
    )
    tem_texto_retrabalho = bool(
        re.search(
            r"(?:retrabalho\s*[*_]*\s*[:\|]\s*[*_]*\s*(?:sim|true|s|yes)|tipo\s*[*_]*\s*[:\|]\s*[*_]*\s*(?:corre[çc][aã]o|retrabalho)|classifica[çc][aã]o\s*[*_]*\s*[:\|][^\n]*retrabalho|\[x\]\s*(?:corre[çc][aã]o|retrabalho))",
            body,
            re.IGNORECASE,
        )
    )
    is_retrabalho = tem_label_correcao or tem_texto_retrabalho

    origem_match = re.search(
        r"(?:issue\s+de\s+origem|origem)\s*[*_]*\s*[:\|]\s*[*_]*\s*#?([0-9]+)",
        body,
        re.IGNORECASE,
    )
    issue_origem = origem_match.group(1) if origem_match else None

    causa_match = re.search(
        r"(?:causa(?:\s+raiz)?(?:\s+do\s+retrabalho)?)\s*[*_]*\s*[:\|]\s*[*_]*\s*([^\n]+)",
        body,
        re.IGNORECASE,
    )
    causa_retrabalho = causa_match.group(1).strip() if causa_match else None

    tabela_contribuicao = _extract_contribution_table(body, num)

    return {
        "number": num,
        "title": item.get("title", f"Issue #{num}"),
        "state": item.get("state", "open"),
        "closed_at": closed_at,
        "closed_date": closed_date,
        "estimativa": estimativa,
        "janela_raw": janela_raw,
        "janela_date": janela_date,
        "milestone": ms_title,
        "labels": labels,
        "criterios": criterios,
        "is_retrabalho": is_retrabalho,
        "issue_origem": issue_origem,
        "causa_retrabalho": causa_retrabalho,
        "tabela_contribuicao": tabela_contribuicao,
    }


def fetch_github_issues() -> dict[str, dict]:
    """
    Obtém todas as issues do repositório utilizando a biblioteca PyGithub.
    Implementa cache local em '.cache/github_issues.json' para resiliência a offline e rate limits.
    """
    token = get_github_token()
    raw_issues_data = None
    last_error = None

    # Tentativa 1: com token obtido
    # Tentativa 2: anônima (caso o token gere 403 por política de expiração organizacional)
    tentativas = [token, None] if token else [None]

    for auth_token in tentativas:
        try:
            g = _get_github_instance(auth_token)
            repo = g.get_repo(REPO_FULL_NAME)
            issues_paginated = repo.get_issues(state="all")

            data_list = []
            for issue in issues_paginated:
                # Ignora Pull Requests (na API do GitHub PRs aparecem na listagem de issues)
                if issue.pull_request:
                    continue

                # Serializa para formato dicionário
                ms_dict = {"title": issue.milestone.title} if issue.milestone else None
                labels_list = [{"name": lbl.name} for lbl in issue.labels]
                closed_at_str = issue.closed_at.isoformat() if issue.closed_at else None

                data_list.append({
                    "number": issue.number,
                    "title": issue.title,
                    "state": issue.state,
                    "body": issue.body or "",
                    "closed_at": closed_at_str,
                    "milestone": ms_dict,
                    "labels": labels_list,
                })

            raw_issues_data = data_list
            # Salva cache atualizado
            os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(raw_issues_data, f, indent=2, ensure_ascii=False)
            break

        except GithubException as ge:
            last_error = ge
            if ge.status == 403:
                # Pode ser rate limit ou token organizacional não aceito
                continue
        except Exception as e:
            last_error = e
            continue

    # Se não foi possível obter da API, recorre ao cache local
    if raw_issues_data is None:
        if os.path.exists(CACHE_FILE):
            print(
                f"[AVISO] Não foi possível consultar a API do GitHub ({last_error}).\n"
                f"        Utilizando cache local em '{CACHE_FILE}'.",
                file=sys.stderr,
            )
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f:
                    raw_issues_data = json.load(f)
            except Exception as e:
                print(f"[ERRO] Falha ao ler cache local: {e}", file=sys.stderr)
                raw_issues_data = []
        else:
            print(f"[ERRO] Falha na API do GitHub e nenhum cache disponível: {last_error}", file=sys.stderr)
            raw_issues_data = []

    issues_map = {}
    for item in raw_issues_data:
        parsed = _parse_issue_payload(item)
        issues_map[parsed["number"]] = parsed

    return issues_map
