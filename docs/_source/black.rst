==========================
Biblioteca Black
==========================

.. image:: https://img.shields.io/pypi/v/black.svg
    :target: https://pypi.python.org/pypi/black
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/black.svg
    :target: https://pypi.python.org/pypi/black
    :alt: Downloads

.. image:: https://img.shields.io/github/license/psf/black.svg
    :target: https://github.com/psf/black/blob/main/LICENSE
    :alt: License

Black é uma ferramenta de formatação de código Python que visa fornecer um estilo consistente e legível de código automaticamente. Projetado para ser simples e sem configurações excessivas, o Black é uma escolha popular entre desenvolvedores Python para garantir que o código fonte seja formatado de maneira uniforme, sem discussões sobre estilos de formatação.

O principal objetivo do Black é automatizar o processo de formatação de código, eliminando debates sobre estilos de codificação e mantendo a consistência entre diferentes contribuidores de um projeto. Ao seguir as diretrizes do PEP 8, a biblioteca Black produz um código limpo e legível, facilitando a colaboração e a manutenção do código Python.

Recursos principais
-------------------

- **Formatação automática**: Black formata automaticamente o código Python para aderir às diretrizes do PEP 8.
- **Sem configuração**: Black é configurado para fornecer uma formatação consistente sem a necessidade de configuração adicional.
- **Integração simples**: Pode ser facilmente integrado a fluxos de trabalho de desenvolvimento existentes usando ferramentas como pre-commit hooks, IDEs e sistemas de controle de versão.
- **Extensibilidade**: Apesar de ser configurado para um estilo padrão, Black permite alguma customização leve através de opções de linha de comando.
- **Velocidade**: Black é projetado para ser rápido, formatando grandes projetos em questão de segundos.

Uso básico
----------

Instale a biblioteca Black via pip:

.. code-block:: bash

    $ pip install black

Formate um arquivo ou diretório:

.. code-block:: bash

    $ black arquivo.py
    $ black diretório/

Consulte a documentação oficial do Black para opções de linha de comando adicionais e informações detalhadas sobre como integrar o Black em seu fluxo de trabalho de desenvolvimento.

Links
-----

- `Repositório oficial no GitHub <https://github.com/psf/black>`_
- `Documentação oficial <https://black.readthedocs.io>`_
- `PyPI <https://pypi.org/project/black>`_
