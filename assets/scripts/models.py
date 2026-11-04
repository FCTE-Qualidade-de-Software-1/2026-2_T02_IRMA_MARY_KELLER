"""
Modelos de dados estruturados com validação via Pydantic para medições PSM/CID.
"""

from datetime import date
from typing import Any
from pydantic import BaseModel, Field


class ContributionEntry(BaseModel):
    """Representa um lançamento individual de horas extraído da tabela de contribuição de uma issue."""
    membro: str
    usuario_raw: str
    data: str  # Formato AAAA-MM-DD
    horas: float = Field(ge=0.0)
    issue: str


class ParsedIssue(BaseModel):
    """Representa os metadados de uma issue do GitHub após extração."""
    number: str
    title: str
    state: str = "open"
    closed_at: str | None = None
    closed_date: date | None = None
    estimativa: float | None = None
    janela_raw: str | None = None
    janela_date: date | None = None
    milestone: str = "Outras atividades"
    labels: list[str] = Field(default_factory=list)
    criterios: list[str] = Field(default_factory=list)
    is_retrabalho: bool = False
    issue_origem: str | None = None
    causa_retrabalho: str | None = None
    tabela_contribuicao: list[ContributionEntry] = Field(default_factory=list)


class MemberSummary(BaseModel):
    """Resumo individual de esforço de um integrante para a Tabela de Recursos (RC1)."""
    key: str
    nome: str
    github: str
    matricula: str
    horas: float
    relacao_str: str = "-"
    desvio_str: str = "-"
    situacao: str = "Sem dados"
    lancamentos: list[ContributionEntry] = Field(default_factory=list)


class MilestoneIssueRow(BaseModel):
    """Linha da tabela de acompanhamento de estimativas por fase (RC2)."""
    number: str
    title: str
    link_md: str
    estado_str: str
    previsto_str: str
    real_str: str
    he_str: str
    hr_str: str
    desvio_str: str
    situacao: str


class MilestoneGroup(BaseModel):
    """Agrupamento de issues por milestone para o Capítulo 5."""
    nome: str
    horas_totais: float
    issues: list[MilestoneIssueRow] = Field(default_factory=list)
