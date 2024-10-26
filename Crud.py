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
    "ID": ""
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

def listar_adm():
    carregar_usuarios_adm()
    if usuarios_adm:
      for i ,user in enumerate(usuarios_adm,start=1):
        print("USUARIOS CADASTRADOS")
        print(f"{i}-Nome:{user['Nome']} idade:{user['Idade']},telefone:{user['telefone']}")
    else:
        print("Nenhum usuario cadastrados")
    salvar_usuarios_adm()

def atualizar_adm():
    carregar_usuarios_adm()
    usuario = input("Digite o ID do usuário: ")
    if usuario == usuarios_adm['ID']:
        print("Usuário encontrado! ")
        print(f"O que você quer alterar?")
        print("[1] Nome")
        print("[2] Idade")
        print("[3] Email")
        print("[4] Telefone")
        print("[5] Senha")
        option=int(input("\n "))
    else:
        print("Nenhum usuario encontrado com esse ID")
    match (option):
        case 1:
         novo_nome=input("Digite um novo nome")
         usuario['nome']=novo_nome
         print("Nome atualizado com sucesso")
        case 2:
         novo_idade=input("Digite um nova idade")
         usuario['idade']=novo_idade
         print("Idade atualizado com sucesso")
        case 3:
         novo_email=input("Digite um novo email")
         usuario['email']=novo_email
         print("Email atualizado com sucesso")
        case 4:
         novo_tel=input("Digite um novo telefone")
         usuario['telefone']=novo_tel
         print("Telefone atualizado com sucesso")
        case 5:
         nova_senha=input("Digite um nova senha")
         usuario['senha']=nova_senha
         print("Senha atualizado com sucesso")
    salvar_usuarios_adm()


def excluir_adm(index):
    carregar_usuarios_adm()
    if usuarios_adm(index):
     usuarios_adm.pop(index)
     print("usuarios excluidos com sucesso")
    else:
        print("Nenhum usuario encontrado")
    salvar_usuarios_adm()


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
            cadastro_adm()
        case 2:
            listar_adm()
        case 3:
            atualizar_adm()
        case 4:
            excluir_adm()
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

def adicionar_usuario(nome,idade,email,telefone,senha):
    adm={
        "Nome":nome,
        "Idade":idade,
        "email":email,
        "telefone":telefone,
        "senha":senha
    }
    usuarios_adm.append(adm)
    salvar_usuarios_adm()

def cadastro_adm():
    nome=input("Qual nome voce quer cadastrar?")
    idade=int(input("Qual sua idade ?"))
    email=input("Qual seu email:")
    telefone=int(input("Telefone:"))
    senha=int(input("Qual sua senha:"))
    senha_adm=senha
    adicionar_usuario(nome,idade,email,telefone,senha)

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