import time
import os
import main
import crud_functions
from colorama import Fore, Back, Style, init
init(autoreset=True)

def menu_inicial():
    print("                                 ")
    print(Fore.BLUE + Style.BRIGHT + "█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print(Fore.CYAN + Style.BRIGHT + "█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Faça sua denúncia de forma segura!")
    print("                                 ")
    time.sleep(1)
    os.system("cls")

def menu_principal():
    while True:
        print(Fore.YELLOW + "\n" + "=" * 20 + " Menu Principal " + "=" * 20)
        print(Fore.GREEN + "[1]" + Fore.CYAN + " Área de Administrador")
        print(Fore.GREEN + "[2]" + Fore.CYAN + " Denúncia Anônima")
        print(Fore.GREEN + "[3]" + Fore.CYAN + " Sair")
        try:
            escolha = int(input(Fore.LIGHTWHITE_EX + "\n" + "Escolha um para continuar: "))

            match escolha:
                case 1:
                    main.autenticacao_adm()
                case 2:
                    menu_denuncia()
                case 3:
                    print(Fore.LIGHTWHITE_EX + "Encerrando...")
                    time.sleep(1.5)
                    break
                case _:
                    print(Fore.LIGHTMAGENTA_EX + "Escolha uma opção válida!")
                    time.sleep(1)
        except ValueError:
            print(Fore.LIGHTMAGENTA_EX + "Digite um valor válido!")

def menu_denuncia():
    while True:
        print(Fore.YELLOW + "\n" + "="*20, "Denúncia Anônima" + "="*20)
        print(Fore.GREEN + "[1] Realizar Denúncia Anônima")
        print(Fore.GREEN + "[2] Busca por Denúncia")
        print(Fore.GREEN + "[3] Sair")
        try:
            resposta= int(input(Fore.LIGHTWHITE_EX + "Escolha um para continuar:"))

            match resposta:
                case 1:
                    crud_functions.criar_denuncia()
                case 2:
                    protocolo = input(Fore.LIGHTWHITE_EX + "\nInforme o número do protocolo da sua denúncia: ")
                    crud_functions.buscar_denuncias(protocolo)
                case 3:
                    break
                case _:
                    print(Fore.LIGHTMAGENTA_EX + "Digite uma opção válida! ")
        except ValueError:
            print(Fore.LIGHTMAGENTA_EX + "Digite um valor válido!")

def menu_adm():
    while True:
        print(Fore.YELLOW + "\n" + "=" * 20 + "Área de Administrador"+ "=" * 20)
        print(Fore.GREEN + "[1] Cadastrar Administrador")
        print(Fore.GREEN + "[2] Listar Administradores")
        print(Fore.GREEN + "[3] Atualizar Administrador")
        print(Fore.GREEN + "[4] Remover Administrador")
        print(Fore.GREEN + "[5] Listar Todas as Denúncias")
        print(Fore.GREEN + "[6] Atualizar Progresso de Denúncia")
        print(Fore.GREEN + "[7] Remover Denúncia")
        print(Fore.GREEN + "[8] Edição de Categorias")
        print(Fore.GREEN + "[9] Sair")
        try:
            resposta = int(input(Fore.LIGHTWHITE_EX + "Escolha um para continuar:"))

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
                    print(Fore.LIGHTWHITE_EX + "Saindo da area do administrador...")
                    time.sleep(1)
                    break
                case _ :
                    print(Fore.LIGHTMAGENTA_EX + "Digite uma opção válida!")
        except ValueError:
            print(Fore.LIGHTMAGENTA_EX + "Digite um valor válido! ")

def menu_categorias():
    while True:
        print(Fore.YELLOW + "=" * 20 + "Menu de Edição de Categorias" + "=" * 20)
        print(Fore.GREEN + "[1] Criar Nova Categoria")
        print(Fore.GREEN + "[2] Listar Categorias")
        print(Fore.GREEN + "[3] Editar Categoria Existente")
        print(Fore.GREEN + "[4] Remover Categoria")
        print(Fore.GREEN + "[5] Sair")
        resposta = int(input(Fore.LIGHTWHITE_EX + "Escolha um para continuar:"))
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
                time.sleep(1)
            case _:
                print(Fore.LIGHTMAGENTA_EX + "Informe um valor válido! ")
