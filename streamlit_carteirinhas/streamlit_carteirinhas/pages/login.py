
import streamlit as st
from utils.auth import autenticar_usuario

def login_page():
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar_usuario(usuario, senha):
            st.success("Login autorizado!")
            st.session_state.page = 'painel'
            st.experimental_rerun()
        else:
            st.error("Credenciais inválidas.")
