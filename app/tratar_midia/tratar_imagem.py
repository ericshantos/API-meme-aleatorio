# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por tratar imagens PIL e a retorna como JPEG
"""

from io import BytesIO
from PIL import Image
import requests


def processar_imagem(imagem_meme: requests.models.Response) -> BytesIO:
    """
    Processa uma imagem de meme.

    Salva a imagem de meme no formato JPEG com uma qualidade de 70%, utilizando um objeto BytesIO.
    Move o ponteiro de leitura/escrita para o início do objeto BytesIO.

    Args:
        imagem_meme: Objeto de imagem Pillow (PIL) representando o meme.

    Returns:
        meme_io: Objeto BytesIO contendo a imagem do meme processada.
    """

    with Image.open(imagem_meme) as img:

        # Cria uma instância de BytesIO
        meme_io = BytesIO()

        # Salva 'imagem_meme' no formato JPEG
        img.save(meme_io, format="JPEG", quality=70)

        # Move o ponteiro de leitura/escrita para o início do objeto BytesIO
        meme_io.seek(0)

    return meme_io
