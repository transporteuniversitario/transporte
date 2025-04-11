import json

def get_user_data():
    with open("base_de_dados.json", "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    with open("base_de_dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

