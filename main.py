import random
import json_functions
import menu_functions

denuncias = [{
}]

usuarios_adm = [{
}]

categorias_denuncias = {
    "categorias": ["Roubo", "Furto", "Assédio",
                   "Agressão Física", "Fraude", "Tráfico de Drogas",
                   "Vandalismo", "Violência Doméstica", "Discriminação"]
}

def gerar_protocolo():
    protocolo = random.randint(100000, 999999)
    return protocolo
numero_protocolo = gerar_protocolo()

def autenticacao_adm():
    usuarios_adm = json_functions.carregar_usuarios_adm()
    nome_usuario = input("\nInforme seu nome de usuário: ")
    senha = input("Informe sua senha: ")

    username_padrao = "admin"
    senha_padrao = "123456"

    autenticado = any(
        nome_usuario == user.get("username") and senha == user.get("senha")
        for user in usuarios_adm) or nome_usuario == username_padrao and senha == senha_padrao

    if autenticado:
        print("\nAutenticação realizada, bem vindo!")
        menu_functions.menu_adm()
    else:
        print("\nAcesso Negado! ")

def main():
    menu_functions.menu_inicial()
    menu_functions.menu_principal()

if __name__=="__main__":
      main()
