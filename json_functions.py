import json
import os

denuncias = [{
    "categoria": "",
    "data": "",
    "local": "",
    "descricao": "",
    "numero_de_protocolo": "",
    "progresso":""
}]

usuarios_adm = [{
    "nome": "",
    "idade": "",
    "email": "",
    "telefone": "",
    "senha": ""
}]

categorias_denuncias = {
    "categorias": ["Roubo", "Furto", "Assédio",
                   "Agressão Física", "Fraude", "Tráfico de Drogas",
                   "Vandalismo", "Violência Doméstica", "Discriminação"]
}

def salvar_denuncias(denuncias):
    with open("denuncias.json", 'w', encoding='utf-8') as file:
        json.dump(denuncias, file, ensure_ascii=False, indent=4)

def carregar_denuncias():
    if os.path.exists("denuncias.json"):
        with open("denuncias.json", "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Erro ao decodificar o JSON. O arquivo pode estar corrompido.")
                return []
    return []

def salvar_usuarios_adm(usuarios_adm):
    with open("usuarios.json", 'w', encoding='utf-8') as file:
        json.dump(usuarios_adm, file, ensure_ascii=False, indent=4)

def carregar_usuarios_adm():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Erro ao decodificar o JSON. O arquivo pode estar corrompido.")
                return []
    return []

def salvar_categorias(categorias_denuncias):
    with open("categorias.json", 'w', encoding='utf-8') as file:
        json.dump(categorias_denuncias, file, ensure_ascii=False, indent=4)

def carregar_categorias():
    if os.path.exists("categorias.json"):
        with open("categorias.json", "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Erro ao decodificar o JSON. O arquivo pode estar corrompido.")
                return []
    return []
