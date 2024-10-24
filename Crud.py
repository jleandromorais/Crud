import os 
import time
import json
denuncias=[]



def apresentacao():
    print("                                 ") 
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("pedio=faça sua denuncia")
    print("Faça sua denuncia com a gente de forma segura!")
    time.sleep(3)
    os.system("cls")
    
    
#Função do usuario pedir foto,faça uma função que peça ao usuario se ele quer pedir uma foto ou vide



def main():
    apresentacao()
    while True: #QUEM QUISER OPINAR SOBRE O MENU SERIA BOM!POIIS SO ADICIONEI ALGO DIFERENTE NO 6
        
        print("+=============Menu Krust burger===================+")
        print("Ola Bem vindo ao krust Burger,o que voce ira querer? ?")
        print("1.Fazer pedido")
        print("2.Ver os pedidos")
        print("3.Atualizar pedido")
        print("4.Excluir pedido")
        print("5.Rastrear pedido e mostrar statuss")
        print("7.Sair")
        escolha=int(input("Escolha um para continuar:"))


if __name__=="__main__":
      main()
