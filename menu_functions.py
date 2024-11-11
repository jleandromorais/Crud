import time
import os
import main
import crud_functions

def menu_inicial():
    print("                                 ")
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Faça sua denúncia com a gente de forma segura!")
    print("                                 ")
    time.sleep(1)
    os.system("cls")

def menu_principal():
    while True:
        print("\n", "="*20, "Menu Principal", "="*20)
        print("[1] Área de Administrador")
        print("[2] Denúncia Anônima")
        print("[3] Sair")
        try:
            escolha = int(input("\nEscolha um para continuar: "))

            match escolha:
                case 1:
                    main.autenticacao_adm()
                case 2:
                    menu_denuncia()
                case 3:
                    print("Encerrando...")
                    time.sleep(1.5)
                    break
                case _:
                    print("Escolha uma opção válida!")
                    time.sleep(1)
        except ValueError:
            print("Digite um valor válido!")

def menu_denuncia():
    while True:
        print("\n", "="*20, "Denúncia Anônima", "="*20)
        print("[1] Realizar Denúncia Anônima")
        print("[2] Busca por Denúncia")
        print("[3] Sair")
        try:
            resposta= int(input("Escolha um para continuar:"))

            match resposta:
                case 1:
                    crud_functions.criar_denuncia()
                case 2:
                    protocolo = input("\nInforme o número do protocolo da sua denúncia: ")
                    crud_functions.buscar_denuncias(protocolo)
                case 3:
                    break
                case _:
                    print("Digite uma opção válida! ")
        except ValueError:
            print("Digite um valor válido!")
def menu_adm():
    while True:
        print("\n", "=" * 20, "Área de Administrador", "=" * 20)
        print("[1] Cadastrar Administrador")
        print("[2] Listar Administradores")
        print("[3] Atualizar Administrador")
        print("[4] Remover Administrador")
        print("[5] Listar Todas as Denúncias")
        print("[6] Atualizar Progresso de Denúncia")
        print("[7] Remover Denúncia")
        print("[8] Edição de Categorias")
        print("[9] Sair")
        try:
            resposta = int(input("Escolha um para continuar:"))

            match resposta:
                case 1:
                    crud_functions.cadastro_adm()
                case 2:
                    crud_functions.listar_adm()
                case 3:
                    crud_functions.alterar_adm()
                case 4:
                    crud_functions.remover_adm()
                case 5:
                    crud_functions.listar_denuncias()
                case 6:
                    crud_functions.atualizar_progresso()
                case 7:
                    crud_functions.remover_denuncia()
                case 8:
                    menu_categorias()
                case 9:
                    print("Voce esta saindo da area do administrador!")
                    time.sleep(1)
                    break
                case _ :
                    print("Digite uma opção válida!")
        except ValueError:
            print("Digite um valor válido! ")
def menu_categorias():
    while True:
        print("=" * 20, "Menu de Edição de Categorias", "=" * 20)
        print("[1] Criar Nova Categoria")
        print("[2] Listar Categorias")
        print("[3] Editar Categoria Existente")
        print("[4] Remover Categoria")
        print("[5] Sair")
        resposta = int(input("Escolha um para continuar:"))
        match resposta:
            case 1:
                crud_functions.criar_categoria()
            case 2:
                crud_functions.listar_categorias()
            case 3:
                crud_functions.editar_categoria()
            case 4:
                crud_functions.remover_categoria()
            case 5:
                break
            case _:
                print("Informe um valor válido! ")
