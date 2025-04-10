
import streamlit as st
import sqlite3
from hashlib import sha256

st.set_page_config(page_title="Carteirinhas Belmonte", layout="centered")

conn = sqlite3.connect("carteirinhas.db", check_same_thread=False)
cursor = conn.cursor()

# Tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    senha TEXT,
    tipo TEXT DEFAULT 'aluno',
    aprovado INTEGER DEFAULT 0
)
""")
conn.commit()

def gerar_credenciais(nome):
    user = nome.replace(" ", "").lower() + "@belmonte"
    senha = nome.split()[0].lower() + "123456"
    return user, senha

menu = st.sidebar.selectbox("Menu", ["Login", "Cadastro"])

if menu == "Cadastro":
    st.title("Cadastro de Aluno")
    nome = st.text_input("Nome completo")
    if st.button("Cadastrar"):
        usuario, senha = gerar_credenciais(nome)
        senha_hash = sha256(senha.encode()).hexdigest()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, usuario, senha_hash))
        conn.commit()
        st.success(f"Cadastro enviado! Aguarde aprovação. Usuário: {usuario} | Senha: {senha}")

elif menu == "Login":
    st.title("Login")
    email = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        senha_hash = sha256(senha.encode()).hexdigest()
        user = cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha_hash)).fetchone()
        if user:
            if user[5] == 1:
                st.success(f"Bem-vindo, {user[1]}")
                st.write("Sua carteirinha estará disponível em breve.")
            else:
                st.warning("Cadastro pendente de aprovação.")
        else:
            st.error("Credenciais inválidas.")
