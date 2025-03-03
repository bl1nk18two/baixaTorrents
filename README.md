# PyWinAuto Torrent Automation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Exemplo](https://img.shields.io/badge/Status-Exemplo-blue)]()

## Descrição

Este projeto demonstra o uso da biblioteca `pywinauto` para automatizar a adição de arquivos `.torrent` a um cliente BitTorrent. Ele lê um arquivo Excel (`Identificação.xlsx`) para obter informações sobre o diretório dos arquivos `.torrent` e o diretório do programa BitTorrent, e então usa `pywinauto` para interagir com a interface gráfica do cliente BitTorrent para adicionar os arquivos e iniciar o download.

**Atenção:** Este projeto é fornecido como um exemplo para fins educacionais e de demonstração. O uso em produção pode exigir adaptações e testes adicionais para garantir a estabilidade e segurança.

## Funcionalidades Principais

*   **Leitura de arquivo Excel:** Lê o arquivo `Identificação.xlsx` para obter informações sobre os diretórios.
*   **Automação da interface gráfica:** Utiliza `pywinauto` para automatizar a interação com o cliente BitTorrent.
*   **Seleção de arquivos .torrent:** Percorre o diretório especificado e seleciona apenas os arquivos com a extensão `.torrent`.
*   **Adição automática de torrents:** Adiciona os arquivos `.torrent` ao cliente BitTorrent através da interface gráfica.
*   **Criação de diretório "Filmes":** Cria automaticamente um subdiretório "Filmes" dentro do diretório de origem para salvar os arquivos baixados.
*   **Tratamento de erros:** Possui tratamento de erros para lidar com situações como arquivo de identificação ausente ou falhas na automação.

## Pré-requisitos

*   Python 3.6 ou superior
*   Pip (gerenciador de pacotes do Python)
*   Cliente BitTorrent instalado (ex: uTorrent, BitTorrent)
*   `pywinauto` instalado
*   Arquivo Excel `Identificação.xlsx` configurado corretamente.

## Estrutura do Código

*   `main.py`: Arquivo principal que inicia a automação.
*   `physics.py`: Contém a classe `Automacao` que implementa a lógica de automação usando `pywinauto`.
*   `funcoes.py`: Contém funções auxiliares, como `timer` e `arquivos`.


## Contribuição

Este é um projeto de exemplo, mas contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT.

## Autor

*   [Henrique Reis]([Link para seu GitHub](https://github.com/bl1nk18two))
