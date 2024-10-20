import os 
import time
import json
denuncias=[]

def salvar_dados():
    with open('pasta.json', 'w') as file:
        json.dump(denuncias, file)
    print("Dados salvos com sucesso!")

def apresentacao():
    print("                                 ") 
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Peça um pizza=Denunciar incidentes ,coca=probelmas e atividades suspeitas=pizza e coca")
    print("Faça sua denuncia com a gente de forma segura!")
    time.sleep(3)
    os.system("cls")
    

while True:
    apresentacao()
    print("+=============Menu Krust burger===================+")
    print("Ola Bem vindo ao krust Burger,qual seria seu pedido ?")
    print("1.Peça um pizza")
    print("2.coca")
    print("3. Coca e pizza")
    escolha=int(input("Escolha um para continuar:"))
    
