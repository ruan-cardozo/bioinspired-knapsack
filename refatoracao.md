# 📄 Refatoração - Plano e Execução

## ✅ O que será refatorado

- Funções utilitárias de entrada e validação em `main.py`: \
As funções de entradas e validação (`parse_list_input`, parte de `get_manual_input`) podem ser extraídas para um módulo utilitário, reduzindo acoplamento e facilitando testes unitários.
- Lógica de entrada/saída em `main.py`: \
Separar lógica de interação com o usuário da lógica de negócios, criando funções/ módulos distintos.
- Testes unitários: \
Adicionar testes unitários para funções em `knapsack.py` e `genetic_algorithm.py`, garantindo cobertura de código e validação de comportamento esperado.

## ✅ Por que será refatorado

- Reduzir duplicação de código: Centralizando funções utilitárias e de validação, evita-se repetição e facilita a manutenção.
- Melhorar a legibilidade e organização: Separando claramente funções de entrada/saída, lógica de negócio e utilitários, o código fica mais fácil de entender e navegar pelo projeto.
- Aumentar a coesão dos módulos: Cada módulo passa a ter uma responsabilidade clara (ex: `io` para entrada/saída, `utils` para utilidades, `knapsack` e `genetic_algorithm` para lógica principal).
- Facilitar a manutenção e evolução: Com responsabilidades bem definidas e menos acoplamento, futuras alterações ou expansões podem ser feitas com menor risco de impacto em outras partes do sistema.
- Separar contextos de execução: Ao dividir o código em camadas (entrada/saída, lógica, utilitários), torna-se possível testar e evoluir cada parte de forma independente, além de permitir a reutilização de componentes em diferentes cenários.
- Aumentar a confiabilidade: A adição de testes unitários para funções principais garante que o comportamento esperado seja mantido mesmo após mudanças, reduzindo a chance de bugs.

## ✅ Técnicas de refatoração que serão utilizadas

| Técnica                  | Descrição breve                                    | Arquivo(s) afetado(s)                                   | Referência           |
|--------------------------|----------------------------------------------------|---------------------------------------------------------|----------------------|
| Extract Method           | Extrair código repetido em funções próprias        | config.py(numpy random generator)                                                 | Refactoring Guru     |
| Move Function            | Mover funções de utilidade para um novo módulo     | main.py → io.py / utils.py                                    | Refactoring Guru     |
| Replace Magic Number     | Substituir números mágicos por constantes nomeadas | src/genetic_algorithm.py, src/knapsack.py, src/io.py            | Refactoring Guru     |
| Write Unit Tests         | Criar testes unitários para funções principais     | tests/knapsack_test.py, tests/genetic_algorithm_test.py | Refactoring Guru     |

## ✅ Processo adotado

| Processo                | Descrição                                          |
| ---------------------- | --------------------------------------------------  |
| Fork                   | Sim                                                 |
| Branch específica      | Sim - feature/refactor                              |
| Repositório separado   | Sim - [Fork Rep](https://github.com/ruan-cardozo/bioinspired-knapsack)                                              |

---

# 📊 Documentação da Refatoração

## ✅ Partes refatoradas

- `main.py`: removida lógica de entrada/saída e validação, agora delegada para módulos → io.py.
- `src/config.py`: criado para usar somente uma instência do numpy generator.
- `src/io/io.py`: criado para centralizar funções de input/output e validação.
- `src/utils/utils.py`: criado para funções utilitárias, como geração automática de itens.
- `tests/knapsack_test.py`, `tests/genetic_algorithm_test.py`, `tests/io_test.py`, `tests/utils_test.py` : criados para testes unitários.

## ✅ Técnicas aplicadas

- **Extract Method:** Separação de blocos de entrada/saída em funções próprias.
- **Move Function:** Funções de utilidade movidas para módulos adequados.
- **Replace Magic Number:** Magic numbers alterados para constantes nomeadas no início dos arquivos, como DEFAULT_POP_SIZE, BLOCK_SIZE_DEFAULT, FITNESS_INVALID, entre outros, tornando o código mais claro e fácil de manter.
- **Write Unit Tests:** Estrutura de testes criada e implementação dos testes unitários realizada para as funções principais do projeto. Todos os testes estão organizados na pasta tests.

## ✅ Ferramentas utilizadas

- Python padrão
- Organização modular de código
- SonarQube para análise de qualidade
- Pytest/Unittesting para testes unitários
- Pylint para linting e verificação de estilo de código
- Github Copilot para sugestões de refatoração e melhorias

## ✅ Resultados da análise de qualidade

- SonarQube: Aplicado correções sugeridas, como troca de métodos obsoletos do numpy.
- Pylint: Código com 10/10 de qualidade, sem erros ou avisos significativos.
- Testes unitários: 100% de cobertura para funções principais, garantindo que todas as funcionalidades críticas estão testadas e funcionando conforme esperado.

## ✅ Desafios encontrados

- Separação de responsabilidades: Identificar claramente quais funções pertenciam à lógica de negócio, entrada/saída ou utilidades exigiu uma análise cuidadosa do código existente. Para superar isso, realizamos revisões em grupo e discutimos o papel de cada função antes de movê-la para um novo módulo.
- Remoção de números mágicos: Encontrar todos os pontos do código onde números mágicos eram utilizados e substituí-los por constantes nomeadas foi um processo detalhado, especialmente para garantir que o significado de cada valor estivesse claro e consistente em todo o projeto.
- Garantia de retrocompatibilidade: Ao mover funções e alterar a estrutura dos módulos, foi necessário garantir que a integração entre as partes do sistema continuasse funcionando corretamente. Para isso, utilizamos testes unitários e revisamos cuidadosamente as importações e dependências.
- Padronização e estilo: Garantir que todo o time seguisse as mesmas convenções de nomenclatura, organização de arquivos e estilo de código demandou alinhamento e uso de ferramentas como Pylint e SonarQube.

## ✅ Aprendizados

Durante o processo de refatoração, nosso time aprofundou o entendimento sobre diversos conceitos importantes de engenharia de software. Aprendemos, na prática, como pequenas mudanças — como substituir números mágicos por constantes nomeadas — podem tornar o código muito mais legível e fácil de manter, mesmo sendo um detalhe que muitas vezes passa despercebido no dia a dia.

Outro ponto que consideramos bastante relevante foi a importância de extrair métodos e mover funções para módulos mais adequados, respeitando o contexto e a responsabilidade de cada parte do sistema. Isso não só melhorou a organização do projeto, mas também facilitou a colaboração entre os membros do time e a realização de testes unitários.

No geral, percebemos que aplicar técnicas clássicas de refatoração, como separar responsabilidades, modularizar o código e adotar boas práticas de nomenclatura, contribui diretamente para a qualidade, a escalabilidade e a sustentabilidade do projeto a longo prazo. Esses aprendizados certamente serão levados para os próximos desafios do time.

---

# 📂 Estrutura do Repositório

## Antes da Refatoração

```
bioinspired-knapsack/
├── main.py
├── knapsack.py
├── genetic_algorithm.py
└── (pouca ou nenhuma separação de módulos)
```

- Toda a lógica de entrada/saída, validação, utilidades e execução principal estava concentrada em poucos arquivos.
- Não havia separação clara entre lógica de negócio, utilidades e interface.
- Testes unitários ausentes ou misturados.


## Depois da Refatoração

```
bioinspired-knapsack/
├── main.py                       # Ponto de entrada, apenas orquestração
├── src/
│   ├── config.py                 # Instância única do gerador aleatório
│   ├── knapsack.py               # Lógica do problema da mochila
│   ├── genetic_algorithm.py      # Algoritmo genético e operadores
│   ├── io/
│   │   └── io.py                 # Funções de entrada/saída e validação
│   └── utils/
│       └── utils.py              # Funções utilitárias (ex: geração de itens)
├── tests/
│   ├── knapsack_test.py
│   ├── genetic_algorithm_test.py
│   ├── io_test.py
│   └── utils_test.py
|── refatoracao.md                # Documentação da refatoração
└── processo.md                  # Processo de refatoração adotado
```

- `main.py` ficou enxuto, delegando responsabilidades para módulos especializados.
- `config.py` centraliza a configuração do gerador aleatório.
- `io.py` concentra toda a lógica de entrada/saída e validação.
- `utils.py` armazena funções utilitárias reutilizáveis.
- `knapsack.py` e `genetic_algorithm.py` focam apenas na lógica principal.
- `tests/` contém todos os testes unitários organizados por módulo.
