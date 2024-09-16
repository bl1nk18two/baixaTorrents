""" Main file """
import sys
from time import sleep

import pandas as pd

import physics

try:
    plan_identificacao = pd.read_excel("Identificação.xlsx", sheet_name='Planilha1', header=0)

    for linha_identificacao in plan_identificacao.index:
        if len(str(plan_identificacao['Diretório'][linha_identificacao]).strip()) > 0:
            diretorio = str(plan_identificacao['Diretório'][linha_identificacao]).strip()
        if len(str(plan_identificacao['Diretório do Programa'][linha_identificacao]).strip()) > 0:
            diretorio_programa = str(plan_identificacao['Diretório do Programa'][linha_identificacao]).strip()
except Exception as a:
    print('Não existe arquivo de identificação!!!', a)
    sleep(10)
    sys.exit()

if __name__ == '__main__':
    try:
        titulo_re = "BitTorrent*"

        aut = physics.Automacao(diretorio_programa, titulo_re)
        aut.seleciona_arquivos(diretorio)
    except Exception as e:
        print(e)
    else:
        physics.timer(10)
        
