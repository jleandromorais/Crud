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
