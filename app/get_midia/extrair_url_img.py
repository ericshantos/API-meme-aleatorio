# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por extrai as URLs das imagens.
"""


from bs4 import BeautifulSoup
import requests


def extrair_urls_imagens(resposta: requests.models.Response) -> list[str]:
    """
    Extrai URLs de imagens de memes de uma resposta HTML.

    Args:
        - resposta (requests.models.Response): Resposta HTML de uma requisição web.

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
