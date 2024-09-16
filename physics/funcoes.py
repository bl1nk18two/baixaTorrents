""" This file holds functions """

from time import sleep
import sys
import os
import glob


def timer(numero):
    """ Timer no terminal """
    contador = int(numero)
    while contador >= 0:
        sleep(1)
        sys.stdout.write(f'\rEncerrando em {contador} Segundos.')
        sys.stdout.flush()
        contador -= 1


def arquivos(caminho):
    """ Percorre todos os arquivos do diretorio e seleciona apenas os que possuem a extensão '.torrent' """
    lista_arquivos = []
    for root, _, _ in os.walk(caminho):
        file_validado = glob.glob(os.path.join(root, '*.torrent'))
        lista_arquivos.append(file_validado)
    files = [item for lista in lista_arquivos for item in lista]
    return files
