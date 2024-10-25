import os 
import time
import json
from http.client import responses

 
denuncia ={
    'Categoria':'',
    'Data':'',
    'Local':'',
    'Descrição':'',
    'Número de Protocolo':''
}
usuarios_adm ={
    'Nome':'',
    'Idade':'',
    'Email':'',
    'Telefone':'',
    'Senha':''
}

categorias_denuncias = {
    'Categorias':['Roubo', 'Furto', 'Assédio',
                  'Agressão Física', 'Fraude', 'Tráfico de Drogas',
                  'Vandalismo', 'Violência Doméstica', 'Discriminação']
}


with open('categorias_denuncias.json', 'w', encoding='utf-8') as file:
    json.dump(categorias_denuncias, file, ensure_ascii=False, indent=4)

with open('denuncias.json', 'w', encoding='utf-8') as file:
    json.dump(denuncia, file, ensure_ascii=False, indent=4)

with open("usuarios_adm.json",'w', encoding='utf-8') as file:
    json.dump(usuarios_adm, file, ensure_ascii=False, indent=4)

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

def listar_adm():
    if usuarios:
      for i ,user in enumerate(usuarios,start=1):
        print("USUARIOS CADASTRADOS")
        print(f"{i}-Nome:{user['Nome']} idade:{user['Idade']},telefone:{user['telefone']}")
    else:
        print("Nenhum usuario cadastrados")


        
def mudar_nome_adm(index):
    if usuarios[index]:
        usuario=usuarios[index]   
        print(f"Qual voce ira alterar {usuario['Nome']} quer alterar:")
        print("1.nome")
        print("2.Idade")
        print("3.email")
        print("4.telefone")
        print("5.Senha")
        op=int(input("Qual função voce quer escolher:"))
    else:
        print("Nenhum usuario encontrado com esse ID")
        
        
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
   

def excluir_adm(index):
    if usuarios(index):
     usuarios.pop(index)
     print("usuarios excluidos com sucesso")
    else:
        print("Nenhum usuario encontrado")

       
    
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
    escolha2 = int(input("Escolha um para continuar:"))
 
    
    match (escolha2):
        case 1:#Terminei primeira funçao ,adicionar
            cadastro_adm()
        case 2:
            listar_adm()
        case 3:
            listar_adm()
            index=int(input("Qual voce queer mudar?"))-1
            mudar_nome_adm(index)
        case 4:
            listar_adm()
            index=int(input("qual voce quer apagar?"))
            excluir_adm(index)
       # case 5:
            #em trabalho
        #case 6:
        #
        #case 7:
        
        case 8:
            editar_categoria()
        case 9:
            print("Voce esta saindo da area do administrador!✌")
            break
            

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
  
def cadastro_adm():    
  nome=input("Qual nome voce quer cadastrar?")
  idade=int(input("Qual sua idade ?"))
  email=input("Qual seu email:")
  telefone=int(input("Telefone:"))
  senha=int(input("Qual sua senha:"))
  senha_adm=senha
  adm1(nome,idade,email,telefone,senha)  
        

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

