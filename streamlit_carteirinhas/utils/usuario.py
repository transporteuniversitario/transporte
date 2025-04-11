import json

def get_user_data():
    try:
        with open("base_de_dados.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print("Erro ao carregar base_de_dados.json:", e)
        return None
