# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Flask API que retorna memes aleatórios de programação.
"""

import random
from flask import Flask
import get_midia, tratar_midia

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
    Rota para obter um meme aleatório.

    Retorna:
        Um arquivo de mídia (imagem) contendo um meme aleatório.
    """
    # Obtém a lista de URLs de memes aleatórios
    lista_meme = get_midia.get_meme_aleatorio()

    # Verifica se a lista de memes é válida
    if lista_meme:
        # URL do meme aleatório
        url_meme = random.choice(lista_meme)

        # Solicita o meme aleatório para memedroid
        repescagem_meme = get_midia.requisicao_memedroid(url_meme, valor_stream=True)

        return tratar_midia.send_file_meme(repescagem_meme)


if __name__ == "__main__":
    app.run(debug=False)
