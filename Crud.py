import os
import time
import json
import random
import crud_functions
from http.client import responses

denuncias = [{
    "Categoria": "",
    "Data": "",
    "Local": "",
    "Descrição": "",
    "Número de Protocolo": "",
    "Progresso": ""
}]
usuarios_adm = [{
    "Nome": "",
    "Idade": "",
    "Email": "",
    "Telefone": "",
    "Senha": "",

}]
categorias_denuncias = [{
    'Categorias':['Roubo', 'Furto', 'Assédio',
                  'Agressão Física', 'Fraude', 'Tráfico de Drogas',
                  'Vandalismo', 'Violência Doméstica', 'Discriminação']
}]

senha_adm = 123456

def salvar_categorias():
    with open('categorias_denuncias.json', 'w', encoding='utf-8') as file:
        json.dump(categorias_denuncias, file, ensure_ascii=False, indent=4)

def salvar_denuncias():
    with open('denuncias.json', 'w', encoding='utf-8') as file:
        json.dump(denuncias, file, ensure_ascii=False, indent=4)

def salvar_usuarios_adm():
    with open("usuarios_adm.json",'w', encoding='utf-8') as file:
        json.dump(usuarios_adm, file, ensure_ascii=False, indent=4)
        print("Salvo com sucesso! ")

def carregar_categorias():
    with open('categorias_denuncias.json', 'r') as file:
        json.load(file)

def carregar_denuncias():
    with open('denuncias.json', 'r') as file:
        json.load(file)

def carregar_usuarios_adm():
    with open('usuarios_adm.json', 'r') as file:
        json.load(file)

def gerar_protocolo():
    protocolo = random.randint(10000, 99999)
    return protocolo

numero_protocolo = gerar_protocolo()

def apresentacao():
    print("                                 ")
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Faça sua denúncia com a gente de forma segura!")
    print("                                 ")
    time.sleep(1)
    os.system("cls")

def menu_denuncia():
    print("="*20, "Denúncia Anônima", "="*20)
    print("[1] Realizar Denúncia Anônima")
    print("[2] Busca por Denúncia")
    print("[3] Sair")
    escolha1= int(input("Escolha um para continuar:"))




def menu_adm():
  while True:
    print("="*20, "Área de Administrador", "="*20)
    print("[1] Cadastrar Administrador")
    print("[2] Listar Administradores")
    print("[3] Atualizar Administrador")
    print("[4] Remover Administrador")
    print("[5] Listar Todas as Denúncias")
    print("[6] Atualizar Progresso de Denúncia")
    print("[7] Remover Denúncia")
    print("[8] Edição de Categorias")
    print("[9] Sair")
    resposta = int(input("Escolha um para continuar:"))

    match (resposta):
        case 1:
            crud_functions.cadastro_adm()
        case 2:
            crud_functions.listar_adm()
        case 3:
            crud_functions.mudar_dados_adm()
        case 4:
            crud_functions.excluir_adm()
        case 5:
            crud_functions.listar_denuncias()
        case 6:
            crud_functions.atualizar_progresso()
        case 7:
            crud_functions.remover_denuncia()
        case 8:
            crud_functions.editar_categoria()
        case 9:
            print("Voce esta saindo da area do administrador!✌")
            time.sleep(1)
            break


def menu_categorias():
    while True:
        print("="*20, "Área de Administrador", "="*20)
        print("[1] Criar Categoria de Denúncia")
        print("[2] Listar Categorias")
        print("[3] Editar Categoria")
        print("[4] Remover Categoria")
        print("[5] Sair")
        resposta = int(input("Escolha um para continuar:"))

        match(resposta):
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

def main():
    crud_functions.carregar_dados_iniciais()
    apresentacao()
    while True:
        print("\n[1] Área de Administrador")
        print("[2] Denúncia Anônima")
        print("[3] Sair")
        escolha = int(input("\nEscolha um para continuar: "))

        match(escolha):
            case 1:
                print("Bem vindo a area ADM!")
                senha=int(input("Insira sua senha: "))
                if senha==senha_adm:
                    menu_adm()
                else:
                    print("\nInfelizmente voce não tem o acesso!✌")
            case 2:
                crud_functions.criar_denuncia_anonima()
            case 3:
                break
if __name__=="__main__":
      main()
