import os 
import time
import json
from http.client import responses

 
denuncia =[]
usuarios =[]

def salvar_adm():
    with open("Administração",'w')as file:
        json.dump(usuarios,file,indent=4)
        print("Salvo com sucesso")
    



categorias_denuncias = {
    'Categorias':['Roubo', 'Furto', 'Assédio', 'Agressão Física', 'Fraude', 'Tráfico de Drogas',
                  'Vandalismo', 'Violência Doméstica', 'Discriminação']
}


with open('categorias_denuncias.json', 'w', encoding='utf-8') as arquivo:
    json.dump(categorias_denuncias, arquivo, ensure_ascii=False, indent=4)

with open('denuncias.json', 'w', encoding='utf-8') as arquivo:
    json.dump(denuncias, arquivo, ensure_ascii=False, indent=4)


senha_adm = 123456

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
        
def mudar(index):
    usuario=usuarios[index]   
    print(f"Qual voce ira alterar {usuario['nome']} quer alterar:")
    print("1.nome")
    print("2.Idade")
    print("3.email")
    print("4.telefone")
    print("5.Senha")
    op=int(input("Qual função voce quer escolher:"))
    
    match (op):
        case 1:
         novo_nome=input("Digite um novo nome")
         usuario['nome']=novo_nome
         print("Nome atualizado com sucesso") 
         salvar_adm()
        case 2:
         novo_idade=input("Digite um nova idade")
         usuario['idade']=novo_idade
         print("Idade atualizado com sucesso") 
         salvar_adm()
        
        case 3:     
         novo_email=input("Digite um novo email")
         usuario['email']=novo_email
         print("Email atualizado com sucesso") 
         salvar_adm()
        case 4:
         novo_tel=input("Digite um novo telefone")
         usuario['telefone']=novo_tel
         print("Telefone atualizado com sucesso") 
         salvar_adm()
         
        case 5:    
         nova_senha=input("Digite um nova senha")
         usuario['senha']=nova_senha
         print("Senha atualizado com sucesso") 
         salvar_adm()
         

def excluir(index):
    if usuarios(index):
     usuarios.pop(index)
     print("usuarios excluidos com sucesso")
    else:
        print("Nenhum usuario encontrado")

       
    
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
            listar()
            index=int(print("Qual voce queer mudar?"))-1
            mudar(index)
        case 4:
            listar()
            index=int(print"qual voce quer apagar?")
            excluir(index)

def adm1(nome,idade,email,telefone,senha):
    adm={
        "Nome":nome,
        "Idade":idade,
        "email":email,
        "telefone":telefone,
        "senha":senha
    }
    usuarios.append(adm)
    salvar_adm()               
            
        

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
#Se Ussa assim!!
def denunucias(categoria,data,descricao,protocolo):
   denuncias ={
     'Categoria':categoria,
     'Data': data,
     'Descrição':descricao,
     'Protocolo': protocolo
}
   denuncia.append(denuncias)


if __name__=="__main__":
      main()

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

