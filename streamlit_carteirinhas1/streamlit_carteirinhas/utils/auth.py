
import json

def autenticar_usuario(usuario, senha):
    try:
        with open("base_de_dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        for user in dados["usuarios"]:
            if user["usuario"] == usuario and user["senha"] == senha:
                return user["tipo"]  # "admin" ou "aluno"

    except FileNotFoundError:
        print("Arquivo base_de_dados.json não encontrado.")

    return None
