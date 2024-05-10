# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por enviar a resposta da requisição GET.
"""

from typing import Union
from flask import send_file
from .tratar_imagem import processar_imagem
from .tratar_video import processar_video
import requests


def send_file_meme(obj_midia: requests.models.Response) -> Union[bytes, str]:
    """
    Envia um arquivo de mídia como resposta HTTP.

    Args:
        obj_midia: Objeto de mídia a ser enviado.
        mimetype: Tipo de mídia.

    Returns:
        Response: Resposta HTTP contendo o arquivo de mídia.
    """

    content_type = obj_midia.headers.get("content-type", "")

    # Verifica se é uma imagem
    if content_type.startswith("image"):

        retorno_midia = processar_imagem(obj_midia.raw)

    # Verifica se é um vídeo
    elif content_type.startswith("video"):

        retorno_midia = processar_video(obj_midia)

    return send_file(retorno_midia, content_type)
