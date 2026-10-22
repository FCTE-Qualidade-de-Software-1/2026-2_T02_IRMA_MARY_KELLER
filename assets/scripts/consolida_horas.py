import csv

import mkdocs_gen_files

INTEGRANTES = {
    "camilasilvac": {
        "github": "CamilaSilvaC",
        "nome": "Camila Silva Cavalcante",
        "matricula": "232013944",
    },
    "geovannaumbelino": {
        "github": "GeovannaUmbelino",
        "nome": "Geovanna Alves Umbelino",
        "matricula": "232014450",
    },
    "jaugustom": {
        "github": "JAugustoM",
        "nome": "José Augusto Alves de Moraes",
        "matricula": "231026429",
    },
    "luisa12ll": {
        "github": "luisa12ll",
        "nome": "Luísa de Souza Ferreira",
        "matricula": "232014807",
    },
    "menali17": {
        "github": "menali17",
        "nome": "Enzo Menali Vettorato Toledo",
        "matricula": "241011054",
    },
    "pwdrinho": {
        "github": "Pwdrinho",
        "nome": "Pedro Lucas Barbosa da Silva",
        "matricula": "241025710",
    },
}

URL_ISSUES = "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/"
URL_COMMITS = "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author="

with mkdocs_gen_files.open("gestao/horas_consolidadas.md", "w") as f:
    print("# Horas Trabalhadas", file=f)

    for arquivo, membro in INTEGRANTES.items():
        print(
            f"## [{membro['nome']}]({URL_COMMITS}{membro['github']}) - {membro['matricula']}\n",
            file=f,
        )

        print("| Data | Horas Trabalhadas | Issue |", file=f)
        print("| :-: | :-: | :-: |", file=f)

        with open(f"assets/dados/gestao/horas/{arquivo}.csv", "r") as c:
            horas_csv = csv.DictReader(c)

            for row in horas_csv:
                data = row["data"].split("-")
                data = f"{data[2]}/{data[1]}/{data[0]}"

                issue = f"[Issue {row['atividade']}]({URL_ISSUES}{row['atividade']})"

                print(f"| {data} | {row['horas']} | {issue} |", file=f)

        print(file=f)
