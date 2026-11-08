"""
Gráficos em SVG puro, gerados no build e embutidos no painel PSM/CID.
"""

from html import escape

AZUL = "#1865F2"
AZUL_ESCURO = "#0B2149"
AZUL_CLARO = "#C8DAFC"
AZUL_FUNDO = "#EDF3FE"
TEAL = "#14BF96"
CINZA_TEXTO = "#5F6168"
CINZA_GRADE = "#EEEEF0"

ALTURA_AREA = 180
MARGEM_ESQUERDA = 44
MARGEM_TOPO = 16
MARGEM_BASE = 46


def _formatar(valor: float, unidade: str) -> str:
    texto = f"{valor:.1f}".replace(".", ",").removesuffix(",0")
    return f"{texto}{unidade}"


def _teto_da_escala(maior_valor: float) -> float:
    if maior_valor <= 0:
        return 1.0
    for passo in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500):
        teto = passo * 4
        if maior_valor <= teto:
            return float(teto)
    return float(maior_valor * 1.1)


def _linhas_de_grade(largura: float, teto: float, unidade: str) -> list[str]:
    elementos = []
    for indice in range(5):
        valor = teto * indice / 4
        y = MARGEM_TOPO + ALTURA_AREA - ALTURA_AREA * indice / 4
        elementos.append(
            f'<line x1="{MARGEM_ESQUERDA}" x2="{largura - 8}" y1="{y:.1f}" y2="{y:.1f}" '
            f'stroke="{CINZA_GRADE}" stroke-width="1"/>'
        )
        elementos.append(
            f'<text x="{MARGEM_ESQUERDA - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" '
            f'fill="{CINZA_TEXTO}">{_formatar(valor, unidade)}</text>'
        )
    return elementos


def barras_agrupadas(
    titulo_acessivel: str,
    categorias: list[str],
    series: list[tuple[str, str, list[float]]],
    unidade: str = "",
    referencia: tuple[str, float] | None = None,
) -> str:
    quantidade_series = max(len(series), 1)
    largura_grupo = max(96, 40 * quantidade_series + 40)
    largura = MARGEM_ESQUERDA + largura_grupo * max(len(categorias), 1) + 16
    altura = MARGEM_TOPO + ALTURA_AREA + MARGEM_BASE
    maior_valor = max([v for _, _, valores in series for v in valores] + [referencia[1] if referencia else 0])
    teto = _teto_da_escala(maior_valor)

    elementos = _linhas_de_grade(largura, teto, unidade)
    largura_barra = min(34, (largura_grupo - 32) / quantidade_series)

    for posicao, categoria in enumerate(categorias):
        inicio_grupo = MARGEM_ESQUERDA + posicao * largura_grupo
        largura_ocupada = largura_barra * quantidade_series + 6 * (quantidade_series - 1)
        x = inicio_grupo + (largura_grupo - largura_ocupada) / 2
        for nome, cor, valores in series:
            valor = valores[posicao]
            altura_barra = ALTURA_AREA * valor / teto
            y = MARGEM_TOPO + ALTURA_AREA - altura_barra
            elementos.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{largura_barra:.1f}" height="{altura_barra:.1f}" '
                f'rx="4" fill="{cor}"><title>{escape(categoria)}, {escape(nome)}: {_formatar(valor, unidade)}</title></rect>'
            )
            elementos.append(
                f'<text x="{x + largura_barra / 2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-size="11" '
                f'font-weight="700" fill="{AZUL_ESCURO}">{_formatar(valor, unidade)}</text>'
            )
            x += largura_barra + 6
        elementos.append(
            f'<text x="{inicio_grupo + largura_grupo / 2:.1f}" y="{MARGEM_TOPO + ALTURA_AREA + 20}" '
            f'text-anchor="middle" font-size="12" font-weight="700" fill="{AZUL_ESCURO}">{escape(categoria)}</text>'
        )

    if referencia:
        rotulo, valor = referencia
        y = MARGEM_TOPO + ALTURA_AREA - ALTURA_AREA * valor / teto
        elementos.append(
            f'<line x1="{MARGEM_ESQUERDA}" x2="{largura - 8}" y1="{y:.1f}" y2="{y:.1f}" '
            f'stroke="{AZUL_ESCURO}" stroke-width="2" stroke-dasharray="6 4"/>'
        )
        elementos.append(
            f'<text x="{largura - 10}" y="{y - 6:.1f}" text-anchor="end" font-size="11" font-weight="700" '
            f'fill="{AZUL_ESCURO}">{escape(rotulo)}</text>'
        )

    return _svg(titulo_acessivel, largura, altura, elementos)


def barras_horizontais_com_media(
    titulo_acessivel: str,
    rotulos: list[str],
    valores: list[float],
    media: float,
    tolerancia: float,
    unidade: str = " h",
) -> str:
    largura_rotulo = 150
    largura_area = 420
    altura_linha = 30
    largura = largura_rotulo + largura_area + 70
    altura = MARGEM_TOPO + altura_linha * len(rotulos) + 34
    teto = _teto_da_escala(max(valores + [media * (1 + tolerancia)]))

    def posicao_x(valor: float) -> float:
        return largura_rotulo + largura_area * valor / teto

    limite_inferior = posicao_x(media * (1 - tolerancia))
    limite_superior = posicao_x(media * (1 + tolerancia))
    base_faixa = MARGEM_TOPO + altura_linha * len(rotulos)
    elementos = [
        f'<rect x="{limite_inferior:.1f}" y="{MARGEM_TOPO - 6}" width="{limite_superior - limite_inferior:.1f}" '
        f'height="{base_faixa - MARGEM_TOPO + 6}" fill="{AZUL_FUNDO}"/>'
    ]

    for indice, (rotulo, valor) in enumerate(zip(rotulos, valores)):
        y = MARGEM_TOPO + indice * altura_linha
        dentro_da_faixa = media > 0 and abs(valor - media) / media <= tolerancia
        cor = AZUL if dentro_da_faixa else AZUL_ESCURO
        elementos.append(
            f'<text x="{largura_rotulo - 10}" y="{y + 16}" text-anchor="end" font-size="12" '
            f'font-weight="700" fill="{AZUL_ESCURO}">{escape(rotulo)}</text>'
        )
        elementos.append(
            f'<rect x="{largura_rotulo}" y="{y + 4}" width="{posicao_x(valor) - largura_rotulo:.1f}" height="16" '
            f'rx="4" fill="{cor}"><title>{escape(rotulo)}: {_formatar(valor, unidade)}</title></rect>'
        )
        elementos.append(
            f'<text x="{posicao_x(valor) + 6:.1f}" y="{y + 16}" font-size="11" font-weight="700" '
            f'fill="{AZUL_ESCURO}">{_formatar(valor, unidade)}</text>'
        )

    x_media = posicao_x(media)
    elementos.append(
        f'<line x1="{x_media:.1f}" x2="{x_media:.1f}" y1="{MARGEM_TOPO - 6}" y2="{base_faixa}" '
        f'stroke="{TEAL}" stroke-width="2"/>'
    )
    elementos.append(
        f'<text x="{x_media:.1f}" y="{base_faixa + 16}" text-anchor="middle" font-size="11" font-weight="700" '
        f'fill="{AZUL_ESCURO}">média {_formatar(media, unidade)}</text>'
    )
    return _svg(titulo_acessivel, largura, altura, elementos)


def _svg(titulo_acessivel: str, largura: float, altura: float, elementos: list[str]) -> str:
    return (
        f'<svg viewBox="0 0 {largura:.0f} {altura:.0f}" role="img" aria-label="{escape(titulo_acessivel)}" '
        f'xmlns="http://www.w3.org/2000/svg" style="max-width:{largura:.0f}px">'
        + "".join(elementos)
        + "</svg>"
    )
