# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por fazer requisição HTTP e extrair as URLs da resposta.
"""

from typing import Union
from .extrair_url_img import extrair_urls_imagens
from .extrair_url_video import extrair_url_video
import requests


def requisicao_memedroid(url: str, valor_stream=None) -> requests.models.Response:
    """
    Faz uma requisição GET para a URL especificada.

    Envia uma solicitação GET para a página principal da URL fornecida,
    opcionalmente permitindo o streaming do conteúdo da resposta de
    acordo com o valor do parâmetro `valor_stream`.
    Se a requisição demorar mais de 10 segundos, a requisição é inserada.

    Args:
        - url (str): A URL para a qual a requisição GET será feita.
        - valor_stream (bool, optional): Se verdadeiro, permite o streaming
        do conteúdo da resposta. Padrão é None.

    Returns:
        retorno_requisicao: Objeto de resposta da requisição.
    """
    # Envia uma solicitação GET para a página principal
    retorno_requisicao = requests.get(url, stream=valor_stream, timeout=10)

    return retorno_requisicao


def get_meme_aleatorio() -> Union[list, None]:
    """
    Obtém uma lista de URLs de memes relacionados à programação.

    Returns:
        Union[list, None]: Uma lista de URLs de memes relacionados à programação,
        ou None se a requisição falhar ou se não houver memes disponíveis.
    """
    # Faz uma requisição GET para a página de memes relacionados à programação
    retorno_requisicao = requisicao_memedroid(
        "https://pt.memedroid.com/memes/tag/programa%C3%A7%C3%A3o"
    )

    # Verificar se a solicitação foi bem-sucedida (código de status HTTP 200)
    if retorno_requisicao.status_code == 200:

        # Extrai as URLs das imagens e dos vídeos dos memes
        url_midias = extrair_urls_imagens(retorno_requisicao) + extrair_url_video(
            retorno_requisicao
        )

        return url_midias

    else:
        # Se a operação falhar, retorne None
        return None
