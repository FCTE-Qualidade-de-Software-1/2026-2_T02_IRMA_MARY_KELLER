const PADRAO_LEGENDA = /^(Tabela|Figura|Quadro|Gráfico)\s+\d+/;
const PADRAO_NUMERO_SECAO = /^(\d+(?:\.\d+)*\.?)\s+/;
const PADRAO_VERSAO = /^Versão\s+(\d+(?:\.\d+)*)$/;

function marcarLegendas() {
  document.querySelectorAll(".md-typeset p").forEach((paragrafo) => {
    const texto = paragrafo.textContent.trim();
    const primeiroFilho = paragrafo.firstElementChild;
    const comecaComEnfase = primeiroFilho && primeiroFilho.tagName === "EM";
    if (PADRAO_LEGENDA.test(texto) && (comecaComEnfase || paragrafo.style.textAlign === "center")) {
      paragrafo.classList.add("legenda");
    }
  });
}

function destacarNumeroDasSecoes() {
  document.querySelectorAll(".md-typeset h2, .md-typeset h3").forEach((titulo) => {
    const primeiroNo = titulo.firstChild;
    if (!primeiroNo || primeiroNo.nodeType !== Node.TEXT_NODE) return;
    const encontrado = primeiroNo.textContent.match(PADRAO_NUMERO_SECAO);
    if (!encontrado) return;
    const numero = document.createElement("span");
    numero.className = "numero-secao";
    numero.textContent = encontrado[1] + " ";
    primeiroNo.textContent = primeiroNo.textContent.slice(encontrado[0].length);
    titulo.insertBefore(numero, primeiroNo);
  });
}

function dataDaUltimaVersao(tituloHistorico) {
  let elemento = tituloHistorico.nextElementSibling;
  while (elemento && !elemento.querySelector("table") && elemento.tagName !== "TABLE") {
    elemento = elemento.nextElementSibling;
  }
  const tabela = elemento && (elemento.tagName === "TABLE" ? elemento : elemento.querySelector("table"));
  if (!tabela) return null;
  const linhas = tabela.querySelectorAll("tbody tr");
  const ultima = linhas[linhas.length - 1];
  return ultima && ultima.cells[1] ? ultima.cells[1].textContent.trim() : null;
}

function transformarVersaoEmSelo() {
  const titulos = [...document.querySelectorAll(".md-typeset h2")];
  const tituloHistorico = titulos.find((titulo) => titulo.textContent.includes("Histórico de versões"));
  document.querySelectorAll(".md-typeset > p, .md-typeset article > p").forEach((paragrafo) => {
    const encontrado = paragrafo.textContent.trim().match(PADRAO_VERSAO);
    if (!encontrado || paragrafo.dataset.selo) return;
    const selo = document.createElement(tituloHistorico ? "a" : "span");
    selo.className = "selo-versao";
    if (tituloHistorico) {
      selo.href = "#" + tituloHistorico.id;
      selo.title = "Ver o histórico de versões";
    }
    const data = tituloHistorico ? dataDaUltimaVersao(tituloHistorico) : null;
    selo.innerHTML = "<strong>Versão " + encontrado[1] + "</strong>" + (data ? "<span>atualizada em " + data + "</span>" : "");
    paragrafo.textContent = "";
    paragrafo.dataset.selo = "sim";
    paragrafo.classList.add("selo-versao__linha");
    paragrafo.appendChild(selo);
    const proximo = paragrafo.nextElementSibling;
    if (proximo && proximo.tagName === "HR") proximo.remove();
  });
}

function aplicarTemaKhan() {
  marcarLegendas();
  destacarNumeroDasSecoes();
  transformarVersaoEmSelo();
}

if (typeof document$ !== "undefined") {
  document$.subscribe(aplicarTemaKhan);
} else {
  document.addEventListener("DOMContentLoaded", aplicarTemaKhan);
}
