======================
Biblioteca PIL (Python Imaging Library)
======================

.. image:: https://img.shields.io/pypi/v/Pillow.svg
    :target: https://pypi.python.org/pypi/Pillow
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/Pillow.svg
    :target: https://pypi.python.org/pypi/Pillow
    :alt: Downloads

.. image:: https://img.shields.io/github/license/python-pillow/Pillow.svg
    :target: https://github.com/python-pillow/Pillow/blob/main/LICENSE
    :alt: License

PIL (Python Imaging Library) é uma biblioteca Python popular para manipulação de imagens.
Desenvolvida para oferecer uma ampla gama de funcionalidades para processamento de imagem,
PIL é amplamente utilizada em aplicações que envolvem manipulação de imagens, como processamento
de fotos, geração de gráficos, análise de imagem e muito mais.

O principal objetivo do PIL é fornecer uma interface fácil de usar para realizar uma variedade
de operações de processamento de imagem. Desde operações básicas, como redimensionamento e
rotação de imagens, até manipulações avançadas, como filtragem, segmentação e reconhecimento
de padrões, o PIL oferece uma ampla gama de recursos para atender às necessidades de
desenvolvedores e pesquisadores.

Recursos principais
-------------------

- **Manipulação de imagens**: Oferece uma ampla gama de funcionalidades para manipulação de imagens, incluindo carregamento, salvamento, redimensionamento, rotação, filtragem, etc.
- **Suporte a vários formatos de arquivo**: Suporta uma variedade de formatos de arquivo de imagem, incluindo JPEG, PNG, GIF, BMP, TIFF, etc.
- **Interface amigável**: Fornecer uma interface simples e intuitiva para realizar operações de processamento de imagem.
- **Extensibilidade**: É altamente extensível, permitindo a criação de plugins e extensões para estender sua funcionalidade.
- **Documentação abrangente**: Oferece documentação detalhada e exemplos de uso para facilitar o aprendizado e o uso da biblioteca.

Uso básico
----------

Instale a biblioteca PIL (Pillow) via pip:

.. code-block:: bash

    $ pip install Pillow

Carregue e manipule uma imagem usando PIL:

.. code-block:: python

    from PIL import Image

    # Carregar uma imagem
    imagem = Image.open('exemplo.jpg')

    # Redimensionar a imagem
    imagem_redimensionada = imagem.resize((200, 200))

    # Salvar a imagem redimensionada
    imagem_redimensionada.save('exemplo_redimensionado.jpg')

Consulte a documentação oficial da PIL (Pillow) para informações detalhadas sobre como usar a biblioteca e explorar recursos avançados.

Links
-----

- `Repositório oficial no GitHub <https://github.com/python-pillow/Pillow>`_
- `Documentação oficial <https://pillow.readthedocs.io>`_
- `PyPI <https://pypi.org/project/Pillow>`_
