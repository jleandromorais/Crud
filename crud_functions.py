import email
import main
import json
import menu_functions
import json_functions
from json_functions import *

def adicionar_usuario(novo_usuario):
    usuarios_adm = json_functions.carregar_usuarios_adm()
    usuarios_adm.append(novo_usuario)
    json_functions.salvar_usuarios_adm(usuarios_adm)

def cadastro_adm():
    json_functions.carregar_usuarios_adm()
    username = input("Informe o nome de usuário do novo administrador: ")
    nome = input("Informe o nome do novo administrador: ")
    idade = input("Informe a idade do novo administrador: ")
    email = input("Informe o email do novo administrador: ")
    telefone = input("Informe o telefone do novo administrador: ")
    senha = input("Informe a senha do novo administrador: ")
    novo_adm = {
            "username": username,
            "nome": nome,
            "idade": idade,
            "email": email,
            "telefone": telefone,
            "senha": senha
        }
    print("Administrador cadastrado com sucesso!")
    adicionar_usuario(novo_adm)

def listar_adm():
    usuarios_adm = json_functions.carregar_usuarios_adm()
    if usuarios_adm:
        print("\nADMINISTRADORES CADASTRADOS:")
        for i, user in enumerate(usuarios_adm[1:], start=1):
            print("-" * 40)
            print(f"  Usuário {i}:")
            print(f"  Nome de Usuário: {user.get('username')}")
            print(f"  Nome: {user.get('nome')}")
            print(f"  Idade: {user.get('idade')}")
            print(f"  Email: {user.get('email')}")
            print(f"  Telefone: {user.get('telefone')}")
            print("-" * 40)
    else:
        print("Nenhum usuário cadastrado!")

def alterar_adm():
    usuarios_adm = json_functions.carregar_usuarios_adm()
    listar_adm()
    json_functions.carregar_usuarios_adm()
    resposta = int(input("\nQual administrador você quer modificar?"))
    try:
        if 0 < resposta <len(usuarios_adm):
            print(f"\nQual informação você gostaria de alterar?")
            print("[1] Username ")
            print("[2] Nome")
            print("[3] Idade")
            print("[4] Email")
            print("[5] Telefone")
            print("[6] Senha")

            opcao = int(input("\n"))
            campos = ["username", "nome", "idade", "email", "telefone", "senha"]

            if 1 <= opcao <= 6:
                novo_valor = input(f"Digite o novo valor para {campos[opcao - 1]}: ")
                usuarios_adm[resposta][campos[opcao - 1]] = novo_valor
                json_functions.salvar_usuarios_adm(usuarios_adm)
                print("Informação alterada com sucesso!")
            else:
                print("Opção inválida! ")
        else:
            print("Administrador não encontrado!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def remover_adm():
    listar_adm()
    usuarios_adm = json_functions.carregar_usuarios_adm()
    resposta = int(input("\nQual usuário você quer remover? "))
    if 0 < resposta <= len(usuarios_adm):
     usuarios_adm.pop(resposta)
     print("Usuario removido com sucesso! ")
    else:
        print("Nenhum usuario encontrado")
    json_functions.salvar_usuarios_adm(usuarios_adm)

def adicionar_denuncia(nova_denuncia):
    denuncias = json_functions.carregar_denuncias()
    denuncias.append(nova_denuncia)
    json_functions.salvar_denuncias(denuncias)

def criar_denuncia():
    categorias_denuncias = json_functions.carregar_categorias()

    print("Informe a categoria do ocorrido: ")
    listar_categorias()

    if not categorias_denuncias.get("categorias"):
        print("Nenhuma categoria disponível para seleção.")
        return

    try:
        resposta = int(input("Escolha a categoria pelo número: "))
        categorias = categorias_denuncias["categorias"]
        if 1 <= resposta <= len(categorias):
            categoria = categorias[resposta - 1]
        else:
            print("Escolha uma opção válida")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    data = input("Informe a data do ocorrido (DD/MM/AA): ")
    local = input("Informe o local do ocorrido: ")
    descricao = input("Dê uma breve descrição do ocorrido: ")
    protocolo = str(main.numero_protocolo)
    print(f"Obrigado pelas informações, seu protocolo é: {protocolo}")
    progresso = "Em Processamento"

    nova_denuncia = {
        "categoria": categoria,
        "data": data,
        "local": local,
        "descricao": descricao,
        "protocolo": protocolo,
        "progresso": progresso
    }

    adicionar_denuncia(nova_denuncia)

def listar_denuncias():
    denuncias = json_functions.carregar_denuncias()
    if denuncias:
        print("\nLISTA DE DENÚNCIAS:")
        for i, denuncia in enumerate(denuncias, start=1):
            print("-" * 40)
            print(f"Denúncia {i}:")
            print(f"  Categoria: {denuncia.get('categoria', 'Não informado')}")
            print(f"  Data: {denuncia.get('data', 'Não informado')}")
            print(f"  Local: {denuncia.get('local', 'Não informado')}")
            print(f"  Descrição: {denuncia.get('descricao', 'Não informado')}")
            print(f"  Protocolo: {denuncia.get('protocolo')}")
            print(f"  Progresso: {denuncia.get('progresso')}")
            print("-" * 40)
    else:
        print("Nenhuma denúncia encontrada!")

def atualizar_progresso():
    denuncias = json_functions.carregar_denuncias()
    listar_denuncias()
    resposta = int(input("\nQual denúncia você quer alterar o progresso? "))
    try:
        if 0 < resposta < len(denuncias):
                print("Escolha a nova categoria: ")
                print("[1] Em Andamento")
                print("[2] Caso Encerrado ")
                opcao = int(input("\n"))

                while True:
                    match opcao:
                        case 1:
                            novo_progresso = "Em Andamento"
                            break
                        case 2:
                            novo_progresso = "Caso Encerrado"
                            break
                        case _:
                            print("Escolha um número válido! ")

                denuncias[resposta]["progresso"] = novo_progresso
                json_functions.salvar_denuncias(denuncias)
                print("Progresso atualizado com sucesso!")
        else:
            print("Opção inválida! ")

    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def remover_denuncia():
    listar_denuncias()
    denuncias = json_functions.carregar_denuncias()
    resposta = int(input("\nQual denúncia você quer remover? "))
    if denuncias:
        if 0 < resposta <= len(denuncias):
            denuncias.pop(resposta-1)
            print("Denúncia removida com sucesso! ")
        else:
            print("Digite um valor válido! ")
        json_functions.salvar_denuncias(denuncias)

def buscar_denuncias(protocolo_busca):
    denuncias = json_functions.carregar_denuncias()
    for denuncia in denuncias:
        if denuncia.get("protocolo") == protocolo_busca:
            print("\nDenúncia encontrada:")
            print(f"  Categoria: {denuncia.get('categoria', 'Não informado')}")
            print(f"  Data: {denuncia.get('data', 'Não informado')}")
            print(f"  Local: {denuncia.get('local', 'Não informado')}")
            print(f"  Descrição: {denuncia.get('descricao', 'Não informado')}")
            print(f"  Protocolo: {denuncia.get('protocolo', 'Não informado')}")
            print(f"  Progresso: {denuncia.get('progresso', 'Não informado')}")
            break
    print("Nenhuma denúncia encontrada com esse protocolo.")

def criar_categoria():
    categorias_denuncias = json_functions.carregar_categorias()
    categoria_nova = input("\nDigite a nova categoria: ")
    categorias_denuncias["categorias"].append(categoria_nova)
    print("Categoria criada com sucesso!")
    json_functions.salvar_categorias(categorias_denuncias)

def listar_categorias():
    categorias_denuncias = json_functions.carregar_categorias()
    if categorias_denuncias and "categorias" in categorias_denuncias:
        print("\nLISTA DE CATEGORIAS DE DENÚNCIAS:")
        for i, categoria in enumerate(categorias_denuncias["categorias"], start=1):
            print(f"[{i}].{categoria}")
    else:
        print("Nenhuma categoria encontrada!")

def editar_categoria():
    categorias_denuncias = json_functions.carregar_categorias()
    listar_categorias()
    try:
        resposta = int(input("\n Escolha o número da categoria a ser editada: "))
        categorias_lista = categorias_denuncias.get("categorias", [])

        if 0 < resposta <= len(categorias_lista):
            categoria_modificada = input("\nDigite a nova categorias: ")
            categorias_denuncias['categorias'][resposta - 1] = categoria_modificada
            print("Categoria editada com sucesso!")
            json_functions.salvar_categorias(categorias_denuncias)
        else:
            print("Escolha um número de categoria válido")
    except ValueError:
        print("Entrada inválida. Por favor insira um número.")

def remover_categoria():
    listar_categorias()
    categorias_denuncias = json_functions.carregar_categorias()
    if "categorias" in categorias_denuncias:
        categorias_lista = categorias_denuncias["categorias"]

        resposta = int(input("\nQual categoria você quer remover? "))
        if 1 <= resposta <= len(categorias_lista):
            categorias_lista.pop(resposta - 1)
            print("Categoria removida com sucesso! ")
            json_functions.salvar_categorias(categorias_denuncias)
        else:
            print("Digite um valor válido! ")
    else:
        print("Nenhuma categoria encontrada!")
