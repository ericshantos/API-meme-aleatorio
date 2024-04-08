# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Flask API que retorna memes aleatórios de programação
"""

import random
from flask import Flask
from PIL import Image
from app.get_imgs.get_imgs import get_meme_aleatorio, requisicao_memedroid
from app.tratar_imagem_pil.tratar_imagem_pil import send_file_meme


app = Flask(__name__)


@app.after_request
def definir_resposta_cabecalho(retorno):
    """
    Define os cabeçalhos da resposta para evitar o armazenamento em cache.

    Configura os cabeçalhos 'Cache-Control', 'Pragma' e 'Expires'
    para indicar que a resposta não deve ser armazenada em cache.
    Isso é útil para garantir que o GitHub (ou outros caches intermediários)
    busque uma nova versão da imagem toda vez, em vez de retornar uma versão
    em cache.

    Args:
        retorno: Objeto de resposta HTTP.

    Returns:
        response: Objeto de resposta HTTP com os cabeçalhos configurados.
    """
    # Define o cabeçalho Cache-Control para evitar armazenamento em cache.
    retorno.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"

    # Define o cabeçalho Pragma como no-cache para evitar armazenamento em cache.
    retorno.headers["Pragma"] = "no-cache"

    # Define o cabeçalho Expires como 0 para indicar que a resposta expira imediatamente.
    retorno.headers["Expires"] = "0"

    # Retorna o objeto de resposta HTTP modificado com os novos cabeçalhos configurados.
    return retorno


@app.route("/", methods=["GET"])
def retornar_meme():
    """
    Retorna um meme aleatório.

    Faz uma requisição HTTP para obter um meme aleatório do site memedroid.
    A imagem é processada utilizando a função tratar_imagem_pil e retornada como resposta.

    Returns:
        response: Imagem do meme processada.
    """
    # URL do meme aleatório
    url_meme = random.choice(get_meme_aleatorio())

    # Solicita o meme aleatório para memedroid
    repescagem_meme = requisicao_memedroid(url_meme, True)

    # Descodifica o conteúdo da resposta
    repescagem_meme.raw.decode_content = True

    # Abre a resposta HTTP
    meme = Image.open(repescagem_meme.raw)

    # Retorna a imagem processada pelo método tratar_imagem_pil
    return send_file_meme(meme)


if __name__ == "__main__":
    app.run(debug=False)
