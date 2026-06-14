1. Visão Geral do Projeto
O sistema é uma aplicação Desktop desenvolvida em Python voltada para o gerenciamento de culturas agrícolas e plantas. O objetivo principal do software é permitir o controle de ciclos de cultivo, diferenciando plantas que produzem o ano todo daquelas que dependem de estações climáticas específicas, fornecendo ferramentas de validação, filtragem inteligente e persistência de dados em um banco de dados relacional (PostgreSQL).

2. Arquitetura e Padrões de Projeto (Design Patterns)
O projeto foi estruturado seguindo rigorosamente os conceitos da Programação Orientada a Objetos (POO) e padrões arquiteturais de mercado:

2.1. Padrão Arquitetural MVC (Model-View-Controller)
Para garantir o baixo acoplamento e a alta coesão, dividimos o sistema em três camadas independentes:

Model (Modelo): Contém as classes de negócio (Planta, CulturaEstacao, CulturaAnoTodo e o padrão Factory CulturaFactory) e os Enums (NomeEstacao, StatusCultura, TipoCultura). Responsável por manter as regras de domínio.

View (Visão): Construída utilizando a biblioteca gráfica Tkinter. Responsável por capturar a interação do usuário (formulários, listagens, botões de ação dinâmica).

Controller (Controlador): Funciona como um intermediário. Recebe as requisições da View, aplica as regras de validação necessárias e aciona a camada de persistência.

2.2. Padrão Criacional: Factory Method
Para o gerenciamento das culturas, foi implementado o padrão Factory. Como o sistema trabalha com tipos distintos de cultivo (Culturas que duram o ano todo vs. Culturas de Estação), a classe CulturaFactory encapsula a lógica de criação de objetos. Isso permite que novas categorias de cultivo sejam adicionadas futuramente sem a necessidade de modificar o código cliente das Views ou Controllers.

2.3. Persistência de Dados e Padrão DAO (Data Access Object)
O gerenciamento do banco de dados relacional foi isolado em classes DAO (CulturaDAO e PlantaDAO).

Integridade do Banco: A tabela de banco de dados utiliza chaves primárias controladas por um contador sequencial auto-incremental (SERIAL), garantindo que cada registro receba um identificador único de forma nativa e segura.

3. Funcionalidades Destacadas
3.1. Padronização Biológica para nomes científicos
Para evitar inconsistências de digitação e garantir a integridade dos dados biológicos, o sistema intercepta os dados na camada de controle. O campo de "Nome Científico" das plantas passa por um algoritmo automatizado baseado na nomenclatura binomial:

A primeira palavra (Gênero da planta) é convertida automaticamente para ter apenas a primeira letra em maiúsculo (.capitalize()).

O epíteto específico (Espécie) e termos subsequentes são convertidos para letras minúsculas (.lower()).

Espaços em branco sobressalentes e duplicados são limpos da string original antes da gravação física no banco.

3.2. Filtro de Busca Dinâmico Prefixado (Autocomplete)
Nas telas de formulários (FormCultura), as caixas de seleção (Combobox) de plantas e estações possuem escuta de eventos em tempo real (trace). Conforme o usuário digita um caractere:

O sistema aplica um filtro baseado em prefixo (.startswith()).

A listagem interna de opções é reduzida de forma invisível nos bastidores para trazer apenas correspondências exatas que comecem com o caractere digitado.

Aqui não consegui ajeitar direito, logo na 1° letra o teclado já é desabilitado

3.3. Estados de Fluxo Rápido 
Na tela principal de listagem de culturas, a tabela (Treeview) monitora dinamicamente a seleção do usuário. Dependendo do StatusCultura retornado do banco de dados, os botões rápidos de ação Plantar e Colher alteram seu estado visual (normal / disabled) em tempo de execução:

Culturas com ciclo finalizado desativam ambos os botões.

Culturas pendentes liberam exclusivamente o fluxo de plantio.

Culturas plantadas bloqueiam o plantio e liberam a colheita.

4. Tecnologias Utilizadas
Linguagem: Python 3.11

Interface Gráfica: Tkinter / ttk (Nativo)

Banco de Dados: PostgreSQL (Persistência via Driver Psycopg2)

Ambiente de Desenvolvimento:VS Code

5. Diagrama de pastas e arquivos

TRABALHO-FINAL-MATHEUS-WITTE/
├── app.py                            # Arquivo principal que inicia a aplicação
├── teste das classes model.py        # Testes isolados das classes do modelo
│
├── controller/
│   ├── __init__.py                   # Inicializador do pacote controller
│   ├── cultura_control.py            # Regras de negócio e validações de culturas
│   └── planta_control.py             # Regras de negócio e validações de plantas
│
├── dao/
│   ├── __init__.py                   # Inicializador do pacote dao
│   ├── db_config.py                  # Configurações de conexão com o banco de dados
│   ├── generic_dao.py                # Classe base com métodos genéricos de persistência
│   ├── cultura_dao.py                # Consultas SQL e persistência de culturas
│   └── planta_dao.py                 # Consultas SQL e persistência de plantas
│
├── model/
│   ├── __init__.py                   # Inicializador do pacote model
│   ├── planta.py                     # Classe concreta do modelo de Planta
│   ├── CulturaAnoTodo.py             # Subclasse para culturas perenes (Ano Todo)
│   ├── CulturaEstacao.py             # Subclasse para culturas indexadas por Estação
│   ├── CulturaFactory.py             # Fábrica (Factory Method) para criar as culturas
│   ├── estacao_enum.py               # Enumeração das estações
│   ├── status_cultura_enum.py        # Enumeração dos status 
│   └── tipo_cultura_enum.py          # Enumeração dos tipos de cultura
│
└── view/
    ├── __init__.py                   # Inicializador do pacote view
    ├── menu.py                       # Janela do menu principal do sistema
    ├── formulario_cultura.py         # Tela de cadastro/edição de culturas
    ├── listagem_cultura.py           # Tela de listagem de culturas
    ├── formulario_plantas.py         # Tela de cadastro/edição de plantas
    ├── listagem_plantas.py           # Tela de listagem e gerenciamento de plantas
    ├── sobre.py                      # Janela com informações do sistema e autoria

6. Declaração de Uso de IA
6.1: Modelos Usados:
-Gemini 3.5 Flash
-Claude Sonnet 4.6

6.2:Fins:
-Tornar o código e telas mais organizados e limpos visualmente
-Estudar e revisar o projeto da locadora desenvolvido ao decorrer da disciplina de LPOO
-Detecção e compreensão de erros nas telas
-Como implementar o filtro de busca (o que acabou mesmo assim não funcionando como eu queria)

-Toda a implementação final foi escrita, revisada e compreendida pelo autor.

-Cada função tem um breve comentário explicativo para entendermos o que ela faz

-Nesse projeto ocorreu um reforço do aprendizado desenvolvido ao longo da disciplina de Linguagem de Programação Orientada a Objetos