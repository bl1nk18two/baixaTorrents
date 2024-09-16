""" This file holds Automation class """

from time import sleep
import os
from pywinauto.application import Application
from .funcoes import arquivos


class Automacao():
    """ Classe destinada a automatizar o download de torrents """

    def __init__(self, diretorio_programa, titulo_re):
        self.app = Application(backend='uia').start(diretorio_programa)
        self.app = Application(backend='uia').connect(title_re=titulo_re, timeout=20)
        self.main_window = self.app.window(title_re=titulo_re)

    def seleciona_arquivos(self, diretorio):
        """ Realiza o processo que consiste em abrir o diretorio e adicionar ao torrents os arquivos. """
        sucesso = False

        try:
            path = arquivos(diretorio)
            if len(path) == 0:
                print('Não há arquivos para baixar.')
                self.fechar_tela()
            else:
                for file in path:

                    btn_abrir = self.main_window.child_window(title="Adicionar Torrent", control_type="Button").wrapper_object()
                    contador = 0
                    while contador < 10:
                        if btn_abrir.is_enabled():
                            btn_abrir.click()
                            break
                        else:
                            contador += 1
                            sleep(1)

                    pagina_dialogo = self.main_window.child_window(title="Selecione um torrent para abrir", control_type="Window")
                    pagina_dialogo.wait('visible', timeout=20)

                    entry_nome = pagina_dialogo.child_window(title="Nome:", auto_id="1148", control_type="ComboBox")
                    entry_nome.click_input()
                    editar_entry_nome = entry_nome.child_window(title="Nome:", auto_id="1148", control_type="Edit")
                    editar_entry_nome.set_focus()

                    editar_entry_nome.set_edit_text(str(file))
                    btn_abrir = pagina_dialogo.child_window(title="Abrir", auto_id="1", control_type="Button")
                    contador = 0
                    while contador < 10:
                        if btn_abrir.is_enabled():
                            btn_abrir.click()
                            break
                        else:
                            contador += 1
                            sleep(1)

                    nome_arquivo = os.path.basename(file)

                    salvar_combobox = self.main_window.child_window(title=" Salvar Em ", auto_id="1201", control_type="ComboBox")
                    salvar_combobox.wait('visible', timeout=20)
                    salvar_combobox.click_input()
                    editar_diretorio_salvar = salvar_combobox.child_window(title=" Salvar Em ", auto_id="1001", control_type="Edit")
                    editar_diretorio_salvar.set_focus()

                    diretorio_filmes = os.path.join(diretorio, 'Filmes')
                    if not os.path.exists(diretorio_filmes):
                        os.mkdir(diretorio_filmes)

                    editar_diretorio_salvar.type_keys('^a')
                    editar_diretorio_salvar.type_keys('{DEL}')
                    editar_diretorio_salvar.set_edit_text(diretorio_filmes)

                    btn_ok = self.main_window.child_window(title="OK", auto_id="20", control_type="Button")

                    contador = 0
                    while contador < 10:
                        if btn_ok.is_enabled():
                            btn_ok.click()
                            print(f'Arquivo "{nome_arquivo}" adicionado com sucesso.')
                            break
                        else:
                            contador += 1
                            sleep(1)

                sucesso = True

        except Exception as e:
            print(e)
        else:
            if sucesso:
                print('Concluído com sucesso')

    def fechar_tela(self):
        """ Fecha a tela aberta pela classe """
        self.main_window.close()
