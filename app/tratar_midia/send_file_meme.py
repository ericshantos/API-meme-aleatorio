# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por enviar a resposta da requisição GET.
"""

from typing import Union
from flask import Response
import tratar_midia
import requests


def send_file_meme(obj_midia: requests.models.Response) -> Union[Response, bytes]:
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

        retorno_midia, mimetype = (
            tratar_midia.tratar_imagem_pil(obj_midia.raw),
            content_type,
        )

    # Verifica se é um vídeo
    elif content_type.startswith("video"):

        retorno_midia, mimetype = (
            tratar_midia.processar_video(obj_midia),
            "multipart/x-mixed-replace; boundary=frame",
        )

    return Response(retorno_midia, mimetype=mimetype)
