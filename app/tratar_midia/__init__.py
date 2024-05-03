"""
Pacote tratar_imagem

O pacote oferece funcionalidades para processar diferentes tipos de mídia,
como imagens e vídeos.

Módulos:
- processar_video: Contém funções para processar vídeos recebidos como respostas HTTP.
- tratar_imagem_pil: Contém funções para processar imagens de memes utilizando a biblioteca Pillow (PIL).
- send_file_meme: Contém uma função para enviar arquivos de mídia como resposta HTTP.

Exemplo de uso:
    import requests
    from tratar_midia import processar_video, tratar_imagem_pil, send_file_meme

    # Processar um vídeo recebido como resposta HTTP
    video_response = requests.get("http://example.com/video")
    for frame in processar_video(video_response):
        # Processar cada frame do vídeo

    # Processar uma imagem de meme
    meme_response = requests.get("http://example.com/meme.jpg")
    meme_bytes_io = tratar_imagem_pil(meme_response.raw)

    # Enviar um arquivo de mídia como resposta HTTP
    media_response = requests.get("http://example.com/media")
    resposta_http = send_file_meme(media_response)
"""

# Importação interna dos módulos
from .tratar_imagem import tratar_imagem_pil
from .tratar_video import processar_video
from .send_file_meme import send_file_meme

# Código de inicialização
print("O pacote tratar_imagem_pil foi carregado")

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "3.2.0"
