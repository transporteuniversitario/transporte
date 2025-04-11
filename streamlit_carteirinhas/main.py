import streamlit as st
from utils.autenticar import autenticar_usuario
from utils.auth import autenticar_usuario
from pages.aluno import tela_aluno
from pages.gerenciar_admin  import tela_admin

# Inicializa a sessão
if 'usuario' not in st.session_state:
    st.session_state.usuario = None
    st.session_state.tipo = None

st.set_page_config(page_title="Sistema de Carteirinhas", page_icon="\U0001F4C4")
st.title("Sistema de Carteirinhas Digitais")

# Se o usuário ainda não está logado
if st.session_state.usuario is None:
    usuario, senha = st.text_input("Usuário"), st.text_input("Senha", type="password")
    if st.button("Entrar"):
        tipo = autenticar_usuario(usuario, senha)
        if tipo:
            st.session_state.usuario = usuario
            st.session_state.tipo = tipo
            st.experimental_rerun()
        else:
            st.error("Credenciais inválidas.")

# Se o usuário está logado
else:
    if st.session_state.tipo == "admin":
        tela_admin(st.session_state.usuario)
    elif st.session_state.tipo == "aluno":
        tela_aluno(st.session_state.usuario)

    if st.button("Sair"):
        st.session_state.usuario = None
        st.session_state.tipo = None
        st.experimental_rerun()
