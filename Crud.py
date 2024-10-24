import os 
import time
import json
from http.client import responses

denuncias ={
     'Categoria':'',
     'Data': '',
     'Descrição': '',
     'Protocolo': '',
     'Progresso': ''
}
usuarios_adm ={
     'Nome':'',
     'Idade':'',
     'Email':'',
     'Telefone':'',
     'Senha':''
}
categorias_denuncias = {
    'Categorias':['Roubo', 'Furto', 'Assédio', 'Agressão Física', 'Fraude', 'Tráfico de Drogas',
                  'Vandalismo', 'Violência Doméstica', 'Discriminação']
}

with open('categorias_denuncias.json', 'w', encoding='utf-8') as arquivo:
    json.dump(categorias_denuncias, arquivo, ensure_ascii=False, indent=4)

with open('denuncias.json', 'w', encoding='utf-8') as arquivo:
    json.dump(denuncias, arquivo, ensure_ascii=False, indent=4)

with open('usuarios_adm.json', 'w', encoding='utf-8') as arquivo:
    json.dump(usuarios_adm, arquivo, ensure_ascii=False, indent=4)

senha_adm = 123456

def apresentacao():
    print("                                 ") 
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Faça sua denuncia com a gente de forma segura!")
    print("                                 ")
    time.sleep(1)
    os.system("cls")

def main():
    apresentacao()
    while True:
        print("\n[1] Área de Administrador")
        print("[2] Denúncia Anônima")
        print("[3] Sair")
        escolha = int(input("\nEscolha um para continuar: "))

def menu_denuncia():
    print("="*20, "Denúncia Anônima", "="*20)
    print("[1] Realizar Denúncia Anônima")
    print("[2] Busca por Denúncia")
    print("[3] Sair")
    escolha = int(input("Escolha um para continuar:"))

def menu_adm():
    print("="*20, "Área de Administrador", "="*20)
    print("[1] Cadastrar Administrador")
    print("[2] Listar Administradores")
    print("[3] Atualizar Administrador")
    print("[4] Remover Administrador")
    print("[5] Listar Todas as Denúncias")
    print("[6] Atualizar Progresso de Denúncia")
    print("[7] Remover Denúncia")
    print("[7] Edição de Categorias")
    print("[8] Sair")
    escolha = int(input("Escolha um para continuar:"))

def menu_categorias():
    print("="*20, "Área de Administrador", "="*20)
    print("[1] Criar Categoria de Denúncia")
    print("[2] Listar Categorias")
    print("[3] Editar Categoria")
    print("[4] Remover Categoria")
    print("[5] Sair")
    escolha = int(input("Escolha um para continuar:"))

if __name__=="__main__":
      main()

#CRUD 1

#CRUD 2

#CRUD 3
def criar_categoria():
    categoria_nova = input("\nDigite a nova categoria: ")
    categorias_denuncias['Categorias'].append(categoria_nova)
    print("Categoria criada com sucesso!")

def listar_categorias():
    print("\nCategorias Atuais: ")
    for i, Categorias in enumerate(categorias_denuncias['Categorias'], start=1):
        print(f"{i}.{Categorias}")

def editar_categoria():
    listar_categorias()
    resposta = int(input("\n Escolha o número da categoria a ser editada: "))
    categoria_modificada = input("\nDigite a nova categorias: ")
    categorias_denuncias['Categorias'][resposta - 1] = categoria_modificada
    print("Categoria editada com sucesso!")

def remover_categoria():
    listar_categorias()
    resposta = int(input("\n Escolha o número da categoria a ser removida: "))
    categorias_denuncias['Categorias'].pop(resposta-1)
    print("Categoria removida com sucesso!")
