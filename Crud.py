import os 
import time
import json

denuncias =[]
usuarios =[]

def salvar_adm():
    with open("Administração",'w')as file:
        json.dump(usuarios_adm,file,indent=4)
        print("Salvo com sucesso")
    
categorias_denuncias = {
    'Categorias':['Roubo', 'Furto', 'Assédio', 'Agressão Física', 'Fraude', 'Tráfico de Drogas',
                  'Vandalismo', 'Violência Doméstica', 'Discriminação']
}

with open('categorias_denuncias.json', 'w', encoding='utf-8') as arquivo:
    json.dump(categorias_denuncias, arquivo, ensure_ascii=False, indent=4)

senha_adm = 345612

def adm1(nome,idade,email,telefone,senha):
    adm ={
     'Nome':nome,
     'Idade':idade,
     'Email':email,
     'Telefone':telefone,
     'Senha':senha
     }
    usuarios_adm.append(adm)

def apresentacao():
    print("                                 ") 
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Faça sua denuncia com a gente de forma segura!")
    print("                                 ")
    time.sleep(1)
    os.system("cls")



def menu_denuncia():
    print("="*20, "Denúncia Anônima", "="*20)
    print("[1] Realizar Denúncia Anônima")
    print("[2] Busca por Denúncia")
    print("[3] Sair")
    escolha1= int(input("Escolha um para continuar:"))

def listar():
    for i ,adm in enumerate(usuarios,start=1):
        print("USUARIOS CADASTRADOS")
        print(f"{i}-Nome:{adm['nome']} idade:{adm['idade']},telefone:{adm['telefone']}")
def mudar():        



    print("Qual voce quer alterar:")
    print("1.nome")
    print("2.Idade")
    print("3.email")
    print("4.telefone")
    print("5.Senha")
    op=int(input("Qual função voce quer escolher:"))
    
    match (op):
        case 1:
            novo_nome       
            
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
    escolha2 = int(input("Escolha um para continuar:"))
    
    match (escolha2):
        case 1:#Terminei primeira funçao ,adicionar
            nome=input("Qual nome voce quer cadastrar?")
            idade=int(input("Qual sua idade ?"))
            email=input("Qual seu email:")
            telefone=int(input("Telefone:"))
            senha=int(input("Qual sua senha:"))
            senha_adm=senha
            adm1(nome,idade,email,telefone,senha)
        case 2:
            listar()
        case 3:
            print("Qual voce quer alterar:")
            print("1.nome")
            print("2.Idade")
            print("3.email")
            print("4.telefone")
            print("5.Senha")
            
            
        

def menu_categorias():
    print("="*20, "Área de Administrador", "="*20)
    print("[1] Criar Categoria de Denúncia")
    print("[2] Listar Categorias")
    print("[3] Editar Categoria")
    print("[4] Remover Categoria")
    print("[5] Sair")
    escolha3 = int(input("Escolha um para continuar:"))


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
                codigo=int(input("Qual seu codigo?"))
                if codigo==senha_adm:
                    print("+==========================================+")
                    menu_adm()
                    
                    
                else:
                    print("Infelizmente voce não tem o acesso!✌")


#CRUD 2

#CRUD 3
denuncias ={
     'Categoria':'',
     'Data': '',
     'Descrição': '',
     'Protocolo': ''
}


if __name__=="__main__":
      main()
