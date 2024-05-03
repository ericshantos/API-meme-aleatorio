"""
Pacote get_midia

Este pacote fornece funcionalidades para extrair URLs de memes e vídeos relacionados à programação
do site Memedroid (https://pt.memedroid.com/).

Módulos:
    - extrair_url_img: Contém a função extrair_urls_imagens para extrair URLs de imagens de memes.
    - extrair_url_video: Contém a função extrair_url_video para extrair URLs de vídeos.
    - requisicao_memedroid: Contém a função requisicao_memedroid para fazer requisições web.
    - get_meme_aleatorio: Contém a função get_meme_aleatorio para obter memes aleatórios relacionados à programação.
"""

# Importações dos módulos
from .requisicao_http import requisicao_memedroid, get_meme_aleatorio
from .extrair_url_img import extrair_urls_imagens
from .extrair_url_video import extrair_url_video

# Código de inicialização
print("O pacote get_img foi carregado")

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "3.2.0"
