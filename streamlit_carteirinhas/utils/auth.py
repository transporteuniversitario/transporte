import json
import os
from datetime import datetime

USUARIOS_DB = "base_de_dados.json"
ALUNOS_DB = "data/alunos.json"

def autenticar_usuario(usuario, senha):
    if not os.path.exists(USUARIOS_DB):
        return None
    with open(USUARIOS_DB, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    for user in dados.get("usuarios", []):
        if user["usuario"] == usuario and user["senha"] == senha:
            return user["tipo"]
    return None

def autenticar_admin(usuario, senha):
    return autenticar_usuario(usuario, senha) == "admin"

def is_admin_logged_in(usuario):
    return usuario and usuario.endswith("@belmonte")

def logout():
    return None

def load_usuarios():
    if not os.path.exists(USUARIOS_DB):
        return []
    with open(USUARIOS_DB, 'r', encoding='utf-8') as f:
        return json.load(f).get("usuarios", [])

def save_usuarios(usuarios):
    with open(USUARIOS_DB, 'w', encoding='utf-8') as f:
        json.dump({"usuarios": usuarios}, f, indent=4, ensure_ascii=False)

def get_user_data(usuario):
    usuarios = load_usuarios()
    for user in usuarios:
        if user["usuario"] == usuario:
            return user
    return None

def gerar_credenciais_aluno(nome_completo):
    nome_usuario = nome_completo.lower().replace(" ", "") + "@belmonte"
    primeiro_nome = nome_completo.split()[0].lower()
    senha = primeiro_nome + "123456"
    return nome_usuario, senha
