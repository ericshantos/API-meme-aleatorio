# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Pacote responsável por fazer requisição HTTP e extrair as URLs da resposta
"""

import requests
from bs4 import BeautifulSoup


def extrair_urls_imagens(resposta):
    """
    Extrai URLs de imagens de memes de uma resposta HTML.

    Args:
        resposta (requests.models.Response): Resposta HTML de uma requisição web.

    Returns:
        list: Uma lista contendo URLs das imagens de memes encontradas na resposta.
    """
    # Criar um objeto BeautifulSoup para analisar o conteúdo HTML da página
    soup = BeautifulSoup(resposta.content, "html.parser")

    # Encontrar todas as tags de div com a classe 'item-aux-container'
    meme_img_tags = soup.find_all("div", class_="item-aux-container")

    # Imagens
    imgs = []

    for tag in meme_img_tags:

        # Extrair a URL da imagem do meme da tag <img> dentro da tag <div>
        img_tag = tag.find("img", class_="img-responsive")

        if img_tag:
            # Se válida, adiciona a URL na lista imgs
            img_url = img_tag["src"]
            imgs.append(img_url)

    return imgs


def requisicao_memedroid(url, valor_stream=None):
    """
    Faz uma requisição GET para a URL especificada.

    Envia uma solicitação GET para a página principal da URL fornecida, opcionalmente permitindo o streaming
    do conteúdo da resposta de acordo com o valor do parâmetro `valor_stream`.

    Args:
        url (str): A URL para a qual a requisição GET será feita.
        valor_stream (bool, optional): Se verdadeiro, permite o streaming do conteúdo da resposta. Padrão é None.

    Returns:
        retorno_requisicao: Objeto de resposta da requisição.
    """
    # Envia uma solicitação GET para a página principal
    retorno_requisicao = requests.get(url, stream=valor_stream)

    return retorno_requisicao


def get_meme_aleatorio():
    """
    Obtém uma lista de URLs de memes aleatórios relacionados à programação do site Memedroid.

    Faz uma requisição GET para a página que contém memes relacionados à programação no site Memedroid.
    Verifica se a solicitação foi bem-sucedida (código de status HTTP 200).
    Se a solicitação for bem-sucedida, extrai as URLs das imagens dos memes e as retorna como uma lista.
    Caso contrário, retorna None.

    Returns:
        urls_memes (list or None): Lista de URLs das imagens dos memes, ou None se a requisição falhar.
    """
    retorno_requisicao = requisicao_memedroid(
        "https://www.memedroid.com/memes/tag/programming"
    )

    # Verificar se a solicitação foi bem-sucedida (código de status HTTP 200)
    if retorno_requisicao.status_code == 200:

        return extrair_urls_imagens(retorno_requisicao)

    else:
        # Se a operação falhar, retorne None
        return None
