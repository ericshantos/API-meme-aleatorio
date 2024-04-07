"""
Módulo para extração de URLs de imagens de memes relacionados à programação do site Memedroid.

Este módulo contém funções para extrair URLs de imagens de memes relacionados à programação do site Memedroid.
A função `extrair_urls_imagens` recebe uma resposta HTML de uma requisição web e retorna uma lista de URLs
das imagens de memes encontradas na resposta. A função `requisicao_memedroid` faz uma requisição GET para
uma URL especificada, permitindo opcionalmente o streaming do conteúdo da resposta. A função `get_meme_aleatorio`
obtém uma lista de URLs de memes aleatórios relacionados à programação do site Memedroid, fazendo uma requisição
GET para a página que contém esses memes e retornando as URLs das imagens dos memes encontrados, ou None em caso
de falha na requisição.

Exemplo de uso:

    from modulo import extrair_urls_imagens, get_meme_aleatorio

    # Fazer uma requisição para obter URLs de memes relacionados à programação
    urls_memes_programacao = get_meme_aleatorio()

    if urls_memes_programacao:
        # Imprimir as URLs das imagens dos memes
        for url in urls_memes_programacao:
            print(url)
    else:
        print("Falha ao obter memes relacionados à programação.")

"""

# Importações de módulos internos
from .get_meme_aleatorio import get_meme_aleatorio

# Código de inicialização
print("O pacote get_img foi carregado")

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "2.0.0"