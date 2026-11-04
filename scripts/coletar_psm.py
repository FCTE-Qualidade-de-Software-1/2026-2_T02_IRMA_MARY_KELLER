#!/usr/bin/env python3
"""
Script de coleta e cálculo dos indicadores PSM/CID.
Permite executar via CLI conforme especificado no Plano e Procedimento de Medição:
    uv run scripts/coletar_psm.py [--data AAAA-MM-DD] [--out caminho/do/arquivo.md]
"""

import os
import sys

# Adicionar raiz e pasta de scripts ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from assets.scripts.consolida_horas import main

if __name__ == "__main__":
    main()
