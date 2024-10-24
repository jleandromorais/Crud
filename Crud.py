import os 
import time
import json

denuncias = [
    {'Categoria':'',
     'Data': '',
     'Descrição': '',
     'Protocolo': ''}
]

usuarios_adm = [
    {'Nome':'',
     'Idade':'',
     'Email':'',
     'Telefone':'',}
]

categorias_denuncias = [
    {'Categorias':['Roubo', 'Furto', 'Assédio', 'Agressão Física', 'Extorsão']}
]

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

#Função do usuario pedir foto,faça uma função que peça ao usuario se ele quer pedir uma foto ou vide

def main():
    apresentacao()
    while True:
        print("\n[1] Área de Administrador")
        print("[2] Denúncia Anônima")
        print("[3] Denúncias em Andamento")
        print("[4] Sair")
        escolha = int(input("\nEscolha um para continuar: "))

def menu_denuncia():
    print("="*20, "Denúncia Anônima", "="*20)
    print("[1] Realizar Denúncia Anônima")
    print("[2] Denúncias em Andamento")
    print("[3] Sair")
    escolha = int(input("Escolha um para continuar:"))


if __name__=="__main__":
      main()

#CRUD 1

#CRUD 2

#CRUD 3