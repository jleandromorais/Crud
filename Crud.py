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
        print("1.Fazer um pedido")
        print("2.Ver os pedidos")
        print("3.Atualizar pedido")
        print("4.Excluir pedido")
        print("5.Rastrear pedido e mostrar statuss")
        print("7.Sair")
        escolha=int(input("Escolha um para continuar:"))
        match(escolha):
            case 1:
            #precisamos de uma função que pergunte:Nome,idade,texto da ocorrencia,local,senha,E PERGUNTE SE ELE QUER USAR FOTOS OU NÃO,USE IF OU ELID OU ELSE PARA FAZER A PERGUNTA
            #se quiserem adicionar mais ,recomendo ,mostre uma mensaagem exibindo que foi tudo
            #Enzo
       # case 2:
            #Essa funçao vai analisar a ocorrencia e mostrar todas ocorrencias,com todas informaçoes,INCLUSIVE FOTOS e mostre uma mensaagem mostrando todos
            #DPS PERGUNTE AO USUARIO SE ELE QUER MODIFICAR ALGO,SE SIM USE A FUNCAO DO CASE 3
            #KAYKY
            
       # case 3:
            # Peça a senha ,nessa função temos que atualizar a ocorrencia por completo,peça pro usuario para atualizar os itens e mostre uma mensaagem COM FOTOS INCLUSIVE
            #FAÇA UM MINI CRUD PERGUNTANDO QUAL  OPCAO ELE QUER MODIFICAR FAÇA ISSO ATE QUE ELE CLIQUE EM RETOMAR O MENU
            #GABRIEL
       # case 4:
            #FUNÇAO APAGAR,PERGUNTE QUAL SENHA ELE QUER APAGAR E APAGUE A CORRETA, DPS ESCREVA UMA MSG QUE MOSTRE QUAL SENHA FOI APAGADA E QUE MOSTRE AS RESTANTES
            #Levi
        #case 5:
            #DEVE MOSTRAR QUAL PEDIDO PELA SENHA E MOSTRAR OS STATUS(CRIAR UMA CHAVE ALEATORIA COM STATUS EM ADAMENTO,ACOES TOMADAS E RESOLUÇOES FAÇA COM QUE
            #A CADA 2 WHILE MUDE OS STATUS NA SEGJUINTE ORDEM ||ANDAMENTO =>ACOES TOMADDAS (FAÇA TRES ACOES E BOTE NO ALEATORIO)=> RESOLUCOES
            #Leandro
            
if __name__=="__main__":
    main()
