import json

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
