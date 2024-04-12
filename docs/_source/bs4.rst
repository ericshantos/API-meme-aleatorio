======================
Biblioteca BeautifulSoup (bs4)
======================

.. image:: https://img.shields.io/pypi/v/beautifulsoup4.svg
    :target: https://pypi.python.org/pypi/beautifulsoup4
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/beautifulsoup4.svg
    :target: https://pypi.python.org/pypi/beautifulsoup4
    :alt: Downloads

.. image:: https://img.shields.io/github/license/wention/BeautifulSoup4.svg
    :target: https://github.com/wention/BeautifulSoup4/blob/master/LICENSE
    :alt: License

BeautifulSoup (bs4) é uma biblioteca Python para análise de documentos HTML e XML.
Projetada para facilitar a extração de dados de páginas da web, BeautifulSoup é amplamente
utilizada em tarefas de web scraping, análise de dados web e mineração de textos.

O principal objetivo do BeautifulSoup é fornecer uma maneira simples e eficiente de extrair
informações estruturadas de documentos HTML e XML. Com suporte a uma variedade de parsers,
como lxml, html5lib e o próprio parser padrão de Python, BeautifulSoup permite que os
desenvolvedores processem documentos web de forma flexível e confiável.

Recursos principais
-------------------

- **Análise HTML/XML**: Oferece funcionalidades robustas para analisar e navegar em documentos HTML e XML.
- **Seletores poderosos**: Permite selecionar elementos específicos do documento usando seletores CSS ou expressões XPath.
- **Facilidade de uso**: Fornecer uma interface simples e intuitiva para realizar operações de análise e extração de dados.
- **Suporte a diversos parsers**: Suporta vários parsers, permitindo escolher o mais adequado para as necessidades do projeto.
- **Integração com outras bibliotecas**: Pode ser facilmente integrada com outras bibliotecas Python, como requests, para criar poderosos scripts de web scraping.

Uso básico
----------

Instale a biblioteca BeautifulSoup via pip:

.. code-block:: bash

    $ pip install beautifulsoup4

Importe a biblioteca e analise um documento HTML:

.. code-block:: python

    from bs4 import BeautifulSoup

    html = '<html><body><h1>Hello, World!</h1></body></html>'
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.h1.text)

Consulte a documentação oficial do BeautifulSoup para informações detalhadas sobre como usar a biblioteca e explorar recursos avançados.

Links
-----

- `Repositório oficial no GitHub <https://github.com/wention/BeautifulSoup4>`_
- `Documentação oficial <https://www.crummy.com/software/BeautifulSoup/bs4/doc>`_
- `PyPI <https://pypi.org/project/beautifulsoup4>`_
