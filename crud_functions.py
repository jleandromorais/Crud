import json

#CRUD CATEGORIAS
######################################################################################
def criar_categoria():
    categoria_nova = input("\nDigite a nova categoria: ")
    categorias_denuncias['Categorias'].append(categoria_nova)
    print("Categoria criada com sucesso!")
    salvar_categorias()

def listar_categorias():
    print("\nCategorias Atuais: ")
    for i, Categorias in enumerate(categorias_denuncias['Categorias'], start=1):
        print(f"{i}.{Categorias}")
    salvar_categorias()

def editar_categoria():
    listar_categorias()
    resposta = int(input("\n Escolha o número da categoria a ser editada: "))
    categoria_modificada = input("\nDigite a nova categorias: ")
    categorias_denuncias['Categorias'][resposta - 1] = categoria_modificada
    print("Categoria editada com sucesso!")
    salvar_categorias()

def remover_categoria():
    listar_categorias()
    resposta = int(input("\n Escolha o número da categoria a ser removida: "))
    categorias_denuncias['Categorias'].pop(resposta-1)
    print("Categoria removida com sucesso!")
    salvar_categorias()
####################################################################################

#CRUD DENÚNCIAS
####################################################################################
def criar_denuncia_anonima():
    print("\nQual a categoria da sua denúncia? ")
    listar_categorias()
    categoria_denuncia_anonima = input("")
    denuncias['Categoria'].append(categoria_denuncia_anonima)
    salvar_denuncias()

    data_denuncia = input("\nQual a data do ocorrido? ")
    denuncias['Data'].append(data_denuncia)
    salvar_denuncias()

    local_denuncia = input("Qual foi o local do ocorrido? ")
    denuncias['Local'].append(local_denuncia)
    salvar_denuncias()

    descricao_denuncia = input("Descreva o ocorrido: ")
    denuncias['Descrição'].append(descricao_denuncia)
    salvar_denuncias()

    print(f"Usuário administrador criado, seu protocolo é {numero_protocolo}! ")
    denuncias['Protocolo'].append(numero_protocolo)
    salvar_denuncias()

def listar_denuncias():
    print("\nDenùncias Atuais: ")
    for i, denuncia in enumerate(denuncias, start=1):
        print("Denúncias Atuais:")
        print(f"Denúncia [{i}]:")
        for chave, valor in denuncia.items():
            print(f"{chave}: {valor}")
    salvar_denuncias()

def atualizar_progresso():
    listar_denuncias()
    resposta = int(input("\n Escolha a denúncia a ser atualizada: "))
    print("\nDigite o novo progresso: ")
    print("[1] Em Andamento")
    print("[2] Em Resolução")
    print("[3] Caso Encerrado")
    progresso_novo = input("\n ")
    denuncias['Progresso'][resposta - 1] = progresso_novo
    print("Denúncia editada com sucesso!")
    salvar_denuncias()

def remover_denuncia():
    listar_denuncias()
    resposta = int(input("\n Escolha a denúncia a ser removida: "))
    denuncias.remove(resposta-1)
    print("Categoria removida com sucesso!")
    salvar_denuncias()
####################################################################################

#CRUD USUÁRIOS ADM
####################################################################################
def read_json():
    global usuarios
    with open("administracao.json", 'r', encoding='utf-8') as file:
            usuarios = json.load(file)
            print("Dados carregados com sucesso!")
        
def listar_adm():
    if usuarios:
      for i ,user in enumerate(usuarios,start=1):
        print("USUARIOS CADASTRADOS")
        print(f"{i}-Nome:{user['Nome']} idade:{user['Idade']},telefone:{user['telefone']}")
    else:
        print("Nenhum usuario cadastrados")


        
def mudar_dados_adm():
     listar_adm()
     index=int(input("Qual voce queer mudar?"))-1
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

def excluir_adm():
    listar_adm()
    index=int(input("qual voce quer apagar?"))
    if usuarios(index):
     usuarios.pop(index)
     print("usuarios excluidos com sucesso")
    else:
        print("Nenhum usuario encontrado")
def adc_user(nome,idade,email,telefone,senha):
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
  adc_user(nome,idade,email,telefone,senha)  