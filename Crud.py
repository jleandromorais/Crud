import os 
import time
import json

denuncias ={
     'Categoria':'',
     'Data': '',
     'Descrição': '',
     'Protocolo': ''
}
usuarios_adm ={
     'Nome':'',
     'Idade':'',
     'Email':'',
     'Telefone':'',
     'Senha':''
}
categorias_denuncias = {
    'Categorias':['Roubo', 'Furto', 'Assédio', 'Agressão Física', 'Extorsão']
}

with open('categorias_denuncias.json', 'w', encoding='utf-8') as arquivo:
    json.dump(categorias_denuncias, arquivo, ensure_ascii=False, indent=4)

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