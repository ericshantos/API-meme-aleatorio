"""
Módulo para processamento e envio de imagens de memes.

Este módulo fornece funções para processar e enviar imagens de memes. A função `tratar_imagem_pil`
processa uma imagem de meme, salvando-a no formato JPEG com uma qualidade específica e retornando um
objeto BytesIO. A função `send_file_meme` envia um arquivo de imagem JPEG como resposta HTTP,
utilizando a função `tratar_imagem_pil` para processar a imagem do meme e enviar o objeto BytesIO
como resposta HTTP.

Exemplo de uso:

    from modulo import tratar_imagem_pil, send_file_meme
    from PIL import Image

    # Carregar imagem de meme com PIL
    imagem_meme = Image.open('meme.jpg')

    # Processar imagem do meme
    imagem_processada = tratar_imagem_pil(imagem_meme)

    # Enviar imagem do meme como resposta HTTP
    resposta = send_file_meme(imagem_processada)

"""

# Importação interna dos módulos
from .tratar_imagem_pil import tratar_imagem_pil

# Código de inicialização
print('O pacote tratar_imagem_pil foi carregado')

# Definição de __all__
__all__ = ['tratar_imagem_pil']

# Autor
__author__ = 'Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>'

# Versão do pacote
__version__ = '2.0.0'
