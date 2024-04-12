Pre-commit
===========

O pre-commit é uma etapa automatizada que ocorre antes de efetuar um commit (registro de alterações)
em um sistema de controle de versão. Durante essa etapa, uma série de verificações é realizada no código
que está prestes a ser registrado. O objetivo dessas verificações é garantir que o código esteja em
conformidade com determinadas diretrizes, padrões e políticas estabelecidas pela equipe de desenvolvimento.

Funcionamento
---------------

- **Gatilho de Acionamento**: O pre-commit é acionado automaticamente quando um desenvolvedor executa o comando para efetuar um
commit em suas alterações.

- **Verificações Automatizadas**: Durante o pre-commit, uma série de verificações automatizadas é executada
no código modificado. Essas verificações podem incluir:

- **Estilo de Código**: Verifica se o código está formatado de acordo com um estilo de código predefinido.
Convenções de Nomenclatura: Garante que as variáveis, funções e outros elementos de código sigam as convenções de nomenclatura especificadas.

- **Testes Unitários**: Verifica se os testes unitários estão passando.

- **Checagem de Dependências**: Garante que todas as dependências necessárias estejam instaladas e na versão correta.

- **Detecção de Vulnerabilidades**: Verifica se o código contém vulnerabilidades conhecidas de segurança.

- **Análise Estática**: Realiza uma análise estática do código em busca de possíveis problemas, como variáveis não utilizadas, imports desnecessários, entre outros.

- **Feedback ao Desenvolvedor**: Se o código passar por todas as verificações com sucesso, o commit é permitido e prossegue como de costume. Caso contrário, o desenvolvedor é notificado sobre os problemas encontrados e instruído a corrigi-los antes de tentar o commit novamente.

Benefícios do Pre-commit
--------------------------

- **Melhoria da Qualidade do Código**: O pre-commit ajuda a manter um código limpo, consistente e de alta qualidade, ao garantir que ele esteja em conformidade com as diretrizes estabelecidas pela equipe de desenvolvimento.

- **Prevenção de Problemas**: Ao identificar e corrigir problemas no código antes que ele seja registrado no repositório compartilhado, o pre-commit ajuda a evitar a introdução de bugs e problemas de qualidade que possam afetar outros membros da equipe.

- **Padronização**: O pre-commit promove a padronização do código ao garantir que ele siga as convenções de estilo, nomenclatura e outras diretrizes definidas pela equipe.

- **Economia de Tempo**: Ao detectar problemas precocemente, o pre-commit ajuda a economizar tempo que seria gasto na identificação e correção de problemas posteriormente no ciclo de desenvolvimento.


Implementação
---------------

A implementação do pre-commit varia dependendo da ferramenta de controle de versão e das
necessidades específicas do projeto. No entanto, geralmente envolve a criação de scripts
ou configurações que definem as verificações a serem executadas e as ações a serem tomadas
em caso de falha.

No Git, por exemplo, o pre-commit pode ser implementado utilizando ganchos (hooks).
Um script é configurado para ser executado automaticamente sempre que um commit é iniciado.
Este script então executa as verificações necessárias e retorna um código de saída indicando
sucesso ou falha. Se uma falha for detectada, o script pode interromper o commit e fornecer
feedback ao desenvolvedor sobre os problemas encontrados.

Conclusão
-----------

O pre-commit é uma prática valiosa no desenvolvimento de software, ajudando a melhorar
a qualidade do código, prevenir problemas e promover a colaboração eficaz da equipe. Ao
automatizar verificações e garantir a conformidade com padrões e diretrizes estabelecidas,
o pre-commit desempenha um papel crucial na manutenção de código limpo, consistente e confiável
em projetos de software.

hooks
-------

Hook black:
~~~~~~~~~~~~

Descrição: Este gancho usa o Black para formatar automaticamente o código Python de acordo com as diretrizes de estilo recomendadas.

Repositório: `https://github.com/ambv/black <https://github.com/ambv/black>`_

Versão: 24.3.0

Estágio: commit-msg

Versão do Python: 3.8

Hooks próprio do pre-commit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


*Hook check-yaml*:

Descrição: Verifica se os arquivos YAML estão bem formados.

Repositório: `https://github.com/pre-commit/pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_

Versão: v4.6.0

*Hook check-case-conflict*:

Descrição: Verifica se arquivos grandes estão sendo adicionados ao repositório.

Repositório: `https://github.com/pre-commit/pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_

Versão: v4.6.0

*Hook check-merge-conflict*:

Descrição: Verifica se há conflitos de mesclagem deixados em arquivos.

Repositório: `https://github.com/pre-commit/pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_

Versão: v4.6.0

*Hook end-of-file-fixer*:

Descrição: Adiciona uma linha em branco ao final de arquivos sem uma.

Repositório: `https://github.com/pre-commit/pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_

Versão: v4.6.0

*Hook requirements-txt-fixer*:

Descrição: Ordena as dependências no arquivo requirements.txt.

Repositório: `https://github.com/pre-commit/pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_

Versão: v4.6.0

*Hook trailing-whitespace*:

Descrição: Detecta e corrige espaços em branco no final das linhas em arquivos de código-fonte.

Repositório: `https://github.com/pre-commit/pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_

Versão: v4.6.0

*Hook requirements*:

Descrição: Atualiza o arquivo requirements.txt com as dependências do projeto.

Estágio: commit-msg

Hook unittest:
~~~~~~~~~~~~~~~~

Descrição: Executa os testes unitários do projeto.

Estágio: commit

Sempre executa: Sim

Hook commitizen:
~~~~~~~~~~~~~~~~~~

Descrição: Facilita o uso do estilo de mensagem de commit do Commitizen.

Repositório: `https://github.com/commitizen-tools/commitizen <https://github.com/commitizen-tools/commitizen>`_

Versão: v3.21.3

Estágio: commit-msg

Versão do Python: 3.8

Estas são as descrições de cada hook mencionado no arquivo de configuração do pre-commit.
Cada um desempenha um papel específico para melhorar a qualidade e a consistência do código
durante o processo de commit.
