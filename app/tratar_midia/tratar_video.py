# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por tratar os frames de vídeo.
"""

import requests
from io import BytesIO


def processar_video(midia_video: requests.models.Response) -> BytesIO:
    """
    Processa a resposta de um vídeo obtido através de uma requisição HTTP.

    Parameters:
    midia_video (requests.models.Response): A resposta HTTP contendo o vídeo.

    Returns:
    BytesIO: Um objeto BytesIO contendo os bytes do vídeo.

    Raises:
    ValueError: Se a resposta de vídeo for None ou se o conteúdo do vídeo estiver vazio.
    Exception: Qualquer outro erro inesperado durante o processamento do vídeo.
    """
    try:
        if midia_video is None:
            raise ValueError("A resposta de vídeo é None.")

        # Lê o conteúdo do vídeo
        video_bytes = midia_video.content

        # Verifica se o conteúdo do vídeo está vazio
        if not video_bytes:
            raise ValueError("O conteúdo do vídeo está vazio.")

        # Cria um objeto BytesIO para armazenar os bytes do vídeo
        video_io = BytesIO()

        # Escreve os bytes do vídeo no objeto BytesIO
        video_io.write(video_bytes)
        video_io.seek(0)  # Volta para o início do objeto BytesIO

        return video_io

    except ValueError as ve:
        print(f"Erro ao processar o vídeo: {ve}")

    except Exception as e:
        print(f"Erro inesperado ao processar o vídeo: {e}")
