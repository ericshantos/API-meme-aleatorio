"""
Pacote app

Este pacote serve como o ponto de entrada principal da aplicação, utilizando os
pacotes `get_midia` e `tratar_midia` para obter e processar imagens e vídeos de
memes relacionados à programação.
Utiliza as funções `get_meme_aleatorio` do pacote `get_midia` para obter URLs de
memes aleatórios relacionados à programação do site Memedroid e a função `tratar_video`
e `tratar_video` do pacote `tratar_midia` para processar as imagens dos memes obtidos.

Exemplo de uso:

    from app import get_imgs, tratar_imagem_pil

    # Obter URLs de memes aleatórios relacionados à programação
    urls_memes_programacao = get_imgs.get_meme_aleatorio()

    if urls_memes_programacao:
        # Processar as imagens dos memes obtidos
        for url in urls_memes_programacao:
            imagem_meme = get_imgs.requisicao_memedroid(url)
            imagem_processada = tratar_imagem_pil.tratar_imagem_pil(imagem_meme)
            # Faça algo com a imagem processada, como salvá-la ou exibi-la
    else:
        print("Falha ao obter memes relacionados à programação.")

"""

# Código de inicialização
print("O pacote principal app foi carregado")

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "2.1.0"
