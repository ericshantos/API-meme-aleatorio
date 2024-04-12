=======================
Biblioteca Requests
=======================

.. image:: https://img.shields.io/pypi/v/requests.svg
    :target: https://pypi.python.org/pypi/requests
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/requests.svg
    :target: https://pypi.python.org/pypi/requests
    :alt: Downloads

.. image:: https://img.shields.io/github/license/psf/requests.svg
    :target: https://github.com/psf/requests/blob/main/LICENSE
    :alt: License

Requests é uma biblioteca HTTP para Python, projetada para simplificar o envio de solicitações HTTP
e o processamento de respostas. Oferecendo uma API amigável e intuitiva, Requests é amplamente utilizada
por desenvolvedores Python para interagir com APIs da web, acessar recursos remotos e realizar operações de rede.

O principal objetivo do Requests é fornecer uma interface simplificada para realizar operações HTTP, eliminando a
necessidade de lidar diretamente com a complexidade do protocolo. Ao oferecer métodos simples e diretos para enviar
solicitações HTTP e acessar dados de resposta, Requests torna o trabalho com APIs da web e recursos remotos mais
fácil e eficiente.

Recursos principais
-------------------

- **API amigável**: Requests oferece uma API simples e intuitiva para enviar solicitações HTTP e processar respostas.
- **Suporte para métodos HTTP**: Suporta todos os métodos HTTP comuns, como GET, POST, PUT, DELETE, etc.
- **Sessões**: Permite criar sessões persistentes para manter estado entre várias solicitações.
- **Autenticação**: Oferece suporte a vários esquemas de autenticação, incluindo Basic, Digest, OAuth, etc.
- **Gestão de cookies**: Facilita a manipulação de cookies durante solicitações HTTP.
- **Redirecionamento e manipulação de erros**: Lida automaticamente com redirecionamentos e permite o tratamento de erros HTTP.

Uso básico
----------

Instale a biblioteca Requests via pip:

.. code-block:: bash

    $ pip install requests

Envie uma solicitação GET para um URL:

.. code-block:: python

    import requests

    response = requests.get('https://api.example.com/data')

    print(response.status_code)
    print(response.json())

Consulte a documentação oficial do Requests para informações detalhadas sobre como usar a biblioteca e explorar recursos avançados.

Links
-----

- `Repositório oficial no GitHub <https://github.com/psf/requests>`_
- `Documentação oficial <https://docs.python-requests.org>`_
- `PyPI <https://pypi.org/project/requests>`_
