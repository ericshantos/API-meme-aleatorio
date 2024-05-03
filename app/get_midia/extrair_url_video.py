# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por extrai as URLs de vídeos.
"""

from bs4 import BeautifulSoup
import requests


def extrair_url_video(resposta: requests.models.Response) -> list[str]:
    """
    Extrai as URLs de vídeo de uma resposta HTTP.

    Args:
        resposta (requests.models.Response): A resposta HTTP contendo o conteúdo HTML.

    Returns:
        list[str]: Uma lista contendo as URLs de vídeo encontradas na resposta.

    """
    # Analisa o conteúdo HTML da resposta
    soup = BeautifulSoup(resposta.content, "html.parser")

    # Encontra todas as tags <video>
    videos = soup.find_all(
        "video", class_="item-video gallery-item-video grey-background"
    )

    # Lista para armazenar as URLs dos vídeos
    lista_videos = []

    # Verifica se há vídeos presentes
    if videos:
        # Itera sobre as tags <video> encontradas
        for video in videos:

            # Encontra todas as tags <source> dentro de cada tag <video>
            sources = video.find_all("source")

            # Itera sobre as tags <source> encontradas
            for source in sources:

                # Verifica se o tipo de vídeo é "video/webm"
                if source.get("type") == "video/mp4":

                    # Extrai a URL do vídeo e adiciona à lista
                    video_url = source["src"]
                    lista_videos.append(video_url)

    return lista_videos
