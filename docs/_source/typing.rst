==================
Biblioteca typing
==================

.. image:: https://img.shields.io/pypi/v/typing.svg
     :target: https://pypi.python.org/pypi/typing
     :alt: Última Versão

.. image:: https://img.shields.io/pypi/dm/typing.svg
     :target: https://pypi.python.org/pypi/typing
     :alt: Downloads

.. image:: https://img.shields.io/github/license/python/typing.svg
     :target: https://github.com/python/typing/blob/main/LICENSE
     :alt: Licença

A biblioteca typing é uma parte fundamental da biblioteca padrão do Python que fornece suporte para
adicionar anotações de tipos opcionais e obrigatoriedade de tipos (a partir do Python 3.5) ao código
Python. Uma das classes mais úteis fornecidas pela biblioteca typing é a Union, que permite definir
tipos que podem ser um de vários tipos diferentes.

A classe Union é especialmente útil quando se deseja expressar que um determinado valor pode ser de
um tipo ou de outro. Isso é útil em situações em que uma função ou método pode aceitar mais de um
tipo de argumento ou retornar mais de um tipo de valor.

Recursos principais
-------------------

- **Classe Union**: A classe Union permite definir tipos que podem ser um de vários tipos diferentes.

- **Flexibilidade**: Union oferece uma maneira flexível de expressar que um valor pode ser de um tipo
ou de outro.

- **Tipagem segura**: Usar Union ajuda a garantir que os tipos de dados passados para uma função ou
método sejam os esperados, aumentando a segurança e a robustez do código.

- **Melhor documentação**: Ao usar Union, os desenvolvedores podem documentar de forma clara e
explícita os tipos de dados que uma função ou método aceita ou retorna.

- **Compatibilidade**: A classe Union é compatível com outras anotações de tipos fornecidas pela
biblioteca typing, como List, Tuple, Dict etc.

Uso básico
-----------

Para começar a usar a classe Union, importe-a da biblioteca typing em seu código Python:

.. code-block:: python

     from typing import Union

Em seguida, você pode usar Union  para definir tipos que podem ser um de vários tipos diferentes. Por exemplo:

.. code-block:: python

     def process_data(data: Union[str, int]) -> Union[str, int]:
         if isinstance(data, str):
             return data.upper()
         elif isinstance(data, int):
             return data * 2

         result = process_data("hello")
         print(result)  # Saída: HELLO

         result = process_data(5)
         print(result)  # Saída: 10

Consulte a documentação oficial da biblioteca typing para obter mais informações sobre como usar a classe Union e outras anotações de tipos.

Links
------

- `Documentação oficial <https://docs.python.org/3/library/typing.html>`_

- `PyPI <https://pypi.org/project/typing>`_
