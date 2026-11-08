"""
Configurações, constantes e utilitários de data e ambiente para o cálculo de métricas PSM/CID.
Utiliza python-dotenv e python-dateutil para simplificação e robustez.
"""

from datetime import datetime, timedelta, timezone
import os
from dateutil import parser
from dotenv import dotenv_values

TZ_BR = timezone(timedelta(hours=-3))

REPO_FULL_NAME = "FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER"
URL_ISSUES = f"https://github.com/{REPO_FULL_NAME}/issues/"
URL_COMMITS = f"https://github.com/{REPO_FULL_NAME}/commits/main/?author="
CACHE_FILE = ".cache/github_issues.json"
AUTOAVALIACAO_FILE = "assets/dados/gestao/autoavaliacao.csv"

INTEGRANTES = {
    "camilasilvac": {
        "github": "CamilaSilvaC",
        "nome": "Camila Silva Cavalcante",
        "apelido": "Camila Cavalcante",
        "matricula": "232013944",
    },
    "geovannaumbelino": {
        "github": "GeovannaUmbelino",
        "nome": "Geovanna Alves Umbelino",
        "apelido": "Geovanna Umbelino",
        "matricula": "232014450",
    },
    "jaugustom": {
        "github": "JAugustoM",
        "nome": "José Augusto Alves de Moraes",
        "apelido": "José Augusto",
        "matricula": "231026429",
    },
    "luisa12ll": {
        "github": "luisa12ll",
        "nome": "Luísa de Souza Ferreira",
        "apelido": "Luisa de Souza",
        "matricula": "232014807",
    },
    "menali17": {
        "github": "menali17",
        "nome": "Enzo Menali Vettorato Toledo",
        "apelido": "Enzo Menali",
        "matricula": "241011054",
    },
    "pwdrinho": {
        "github": "Pwdrinho",
        "nome": "Pedro Lucas Barbosa da Silva",
        "apelido": "Pedro Lucas",
        "matricula": "241025710",
    },
}

USER_ALIAS_MAP = {}
for chave, dados in INTEGRANTES.items():
    USER_ALIAS_MAP[chave.lower()] = chave
    USER_ALIAS_MAP[dados["github"].lower()] = chave


def normalize_user(user_raw: str) -> str | None:
    """Normaliza username do GitHub (ex: '@CamilaSilvaC' ou 'luisa12ll') para a chave canônica."""
    if not user_raw:
        return None
    clean = user_raw.strip().lstrip("@").lower()
    return USER_ALIAS_MAP.get(clean)


def get_github_token() -> str | None:
    """
    Obtém o token do GitHub.
    Prioriza o token do arquivo .env via python-dotenv para testes locais isolados.
    Se não houver .env ou token nele, utiliza a variável de ambiente GITHUB_TOKEN / GH_TOKEN (usada no CI).
    """
    env_paths = [
        ".env",
        os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
    ]
    for path in env_paths:
        if os.path.exists(path):
            values = dotenv_values(path)
            token = values.get("GITHUB_TOKEN") or values.get("GH_TOKEN")
            if token:
                return token.strip()

    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def parse_date_string(date_raw):
    """Converte strings de data (ex: 21/10/2026, 2026-10-21) para datetime.date via python-dateutil."""
    if not date_raw:
        return None
    try:
        return parser.parse(str(date_raw).strip(), dayfirst=True).date()
    except Exception:
        return None


def format_date_display(dt):
    """Formata datetime.date ou datetime para DD/MM/AAAA."""
    if not dt:
        return "-"
    if isinstance(dt, datetime):
        return dt.strftime("%d/%m/%Y")
    return dt.strftime("%d/%m/%Y")


def parse_closed_datetime(closed_at):
    """Converte a data de fechamento para datetime.date no fuso horário de Brasília."""
    if not closed_at:
        return None
    if isinstance(closed_at, datetime):
        if closed_at.tzinfo is None:
            closed_at = closed_at.replace(tzinfo=timezone.utc)
        return closed_at.astimezone(TZ_BR).date()
    try:
        dt = parser.parse(str(closed_at))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(TZ_BR).date()
    except Exception:
        return None
