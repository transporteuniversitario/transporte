# autenticar.py
import autenticar_usuario
from utils.autenticar
import pandas as pd
import hashlib

def carregar_usuarios():
    try:
        return pd.read_csv("dados/usuarios.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["nome", "email", "senha", "tipo", "aprovado"])

def salvar_usuarios(df):
    df.to_csv("dados/usuarios.csv", index=False)

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def autenticar(email, senha):
    usuarios = carregar_usuarios()
    senha_hash = hash_senha(senha)
    user = usuarios[(usuarios["email"] == email) & (usuarios["senha"] == senha_hash)]
    if not user.empty:
        return user.iloc[0].to_dict()
    return None

def cadastrar_usuario(nome, email, senha, tipo="aluno"):
    usuarios = carregar_usuarios()
    if email in usuarios["email"].values:
        return False
    novo = {
        "nome": nome,
        "email": email,
        "senha": hash_senha(senha),
        "tipo": tipo,
        "aprovado": False if tipo == "aluno" else True
    }
    usuarios = pd.concat([usuarios, pd.DataFrame([novo])], ignore_index=True)
    salvar_usuarios(usuarios)
    return True

def aprovar_usuario(email):
    usuarios = carregar_usuarios()
    usuarios.loc[usuarios["email"] == email, "aprovado"] = True
    salvar_usuarios(usuarios)

def atualizar_valores(email, campo, novo_valor):
    usuarios = carregar_usuarios()
    usuarios.loc[usuarios["email"] == email, campo] = novo_valor
    salvar_usuarios(usuarios)
