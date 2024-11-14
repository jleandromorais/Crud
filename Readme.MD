# Sistema de Denúncias - CRUD

![Status](https://img.shields.io/badge/status-%20finalizado-green)
![Python](https://img.shields.io/badge/python-v3.8+-blue)

Este projeto, desenvolvido para a disciplina **Fundamentos da Computação** com a professora **Aêda Monalliza**, é um sistema CRUD que emula uma aplicação de denúncia policial. O sistema permite a criação de denúncias anônimas, além de fornecer uma área administrativa para o gerenciamento de administradores, categorias de denúncias e progresso das denúncias.

## Índice

- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Execução](#instalação-e-execução)
- [Uso](#uso)
- [Requisitos do Sistema](#requisitos-do-sistema)

## Funcionalidades

### Área Pública
- **Criar Denúncia Anônima**: Usuários podem registrar denúncias de forma anônima. As denúncias são categorizadas, e o progresso delas pode ser atualizado na área administrativa.
- **Buscar Denúncia**: Usuários ao fim de cada denúncia rebem um número de protocolo, na aba de "Buscar Denúncia" é possível verificar os dados da denúncia e o progresso.

### Área de Administrador
- **Gerenciamento de Administradores**:
  - Criar, listar, atualizar ou remover administradores do sistema.
- **Gerenciamento de Denúncias**:
  - Listar, remover ou atualizar o progresso das denúncias.
- **Gerenciamento de Categorias de Denúncia**:
  - Criar, listar, atualizar ou remover categorias de denúncia.

### Outros Recursos
- **Sistema Operacional via Terminal**: Todo o projeto é executado no terminal, sem interface gráfica.
- **Coloração com `Colorama`**: O sistema utiliza a biblioteca `Colorama` para destacar mensagens e melhorar a legibilidade.

## Estrutura do Projeto

```
sistema_denuncias/
├── main.py                   # Arquivo principal do sistema
├── modulos/
│   ├── crud_functions.py     # Funções relacionadas aos CRUD's
│   ├── json_functions.py     # Funções Json
│   ├── main.py               # Arquivo principal do sistema
│   ├── menu_functions.py     # Funções de menus
├── data/
│   ├── categorias.json       # Base de dados JSON para categorias de denúncias
│   ├── denuncias.json        # Base de dados JSON para denúncias efetuadas
│   └── usuarios.json         # Base de dados JSON para usuários administradores
└── README.md                 # Documentação do projeto
```

## Instalação e Execução

### Pré-requisitos

- Python 3.8+
- Biblioteca `Colorama`

### Passos de Instalação

1. **Clone o repositório**:
  ```
  git clone https://github.com/seu_usuario/sistema_denuncias.git
  cd sistema_denuncias
  ```

2. **Instale as dependências**:
  ```
  pip install colorama
  ```

3. **Execute o projeto**:
  ```
  python main.py
  ```

## Uso

### Menu Inicial:

- Denúncia Anônima:
 
  Ao iniciar o programa, os usuários podem optar por criar uma denúncia anônima, selecionando uma categoria e descrevendo a ocorrência.

- Buscar por Denúncias:

  Também na tela inicial, usuários podem buscar suas denúncias pelo número de protocolo gerado ao final de cada denúncia

### Área de Administrador:
Os administradores podem acessar o menu de opções de CRUD para:

- Gerenciar outros administradores.
- Visualizar e modificar o status das denúncias.
- Adicionar, listar, alterar ou remover categorias de denúncia.
- Nota: Cada função é exibida com coloração personalizada (via Colorama) para melhor orientação dos usuários durante a navegação no terminal.

## Requisitos do Sistema
- Python 3.8 ou superior
- Sistema Operacional compatível com Python e terminal que suporte ANSI para exibir cores do Colorama.
