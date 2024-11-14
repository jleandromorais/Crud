# Sistema de Denúncias - CRUD

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-v3.8+-blue)

Este projeto, desenvolvido para a disciplina **Fundamentos da Computação** com a professora **Aêda Monalliza**, é um sistema CRUD que emula uma aplicação de denúncia policial. O sistema permite a criação de denúncias anônimas, além de fornecer uma área administrativa para o gerenciamento de administradores, categorias de denúncias e progresso das denúncias.

## Índice

- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Execução](#instalação-e-execução)
- [Uso](#uso)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Funcionalidades

### Área Pública
- **Criar Denúncia Anônima**: Usuários podem registrar denúncias de forma anônima. As denúncias são categorizadas, e o progresso delas pode ser atualizado na área administrativa.

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

```plaintext
sistema_denuncias/
├── main.py                   # Arquivo principal do sistema
├── modulos/
│   ├── denuncias.py          # Funções CRUD para denúncias
│   ├── administradores.py    # Funções CRUD para administradores
│   ├── categorias.py         # Funções CRUD para categorias de denúncias
│   ├── progresso.py          # Funções para atualizar progresso de denúncias
│   └── utilitarios.py        # Funções utilitárias e configurações da biblioteca Colorama
├── data/
│   ├── denuncias.json        # Base de dados JSON para denúncias
│   ├── administradores.json  # Base de dados JSON para administradores
│   └── categorias.json       # Base de dados JSON para categorias
└── README.md                 # Documentação do projeto
## Instalação e Execução

### Pré-requisitos

- Python 3.8+
- Biblioteca `Colorama`

### Passos de Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/sistema_denuncias.git
   cd sistema_denuncias

2. **Instale as dependências**:
   ```bash
   pip install colorama

3. **Execute o projeto**:
  python main.py

Uso
Denúncia Anônima:
Ao iniciar o programa, os usuários podem optar por criar uma denúncia anônima, selecionando uma categoria e descrevendo a ocorrência.

Área de Administrador:
Os administradores podem acessar o menu de opções de CRUD para:

Gerenciar outros administradores.
Visualizar e modificar o status das denúncias.
Adicionar, listar ou remover categorias de denúncia.
Nota: Cada função é exibida com coloração personalizada (via Colorama) para melhor orientação dos usuários durante a navegação no terminal.
