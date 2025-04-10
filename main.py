import streamlit as st
import pandas as pd
from utils.gerar_carteirinha import gerar_carteirinha
from PIL import Image
import os

st.set_page_config(page_title="Carteirinha Escolar", layout="centered")

st.title("🎓 Sistema de Carteirinhas - Belmonte")

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# Simulação de autenticação
def autenticar(usuario, senha):
    return usuario.endswith("@belmonte") and senha == usuario.split("@")[0] + "123456"

# Login
if not st.session_state["autenticado"]:
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar(usuario, senha):
            st.session_state["autenticado"] = True
            st.session_state["usuario"] = usuario
        else:
            st.error("Credenciais inválidas.")
    st.stop()

st.success(f"Bem-vindo, {st.session_state['usuario']}")

# Formulário da carteirinha
st.subheader("Preencha os dados para gerar a carteirinha:")

nome = st.text_input("Nome completo")
matricula = st.text_input("Matrícula")
curso = st.text_input("Curso")
validade = st.date_input("Validade da carteirinha")
foto = st.file_uploader("Foto do aluno", type=["jpg", "png"])

if st.button("Gerar Carteirinha"):
    if nome and matricula and curso and foto:
        caminho = gerar_carteirinha(nome, matricula, curso, validade, foto)
        st.image(caminho, caption="Carteirinha Gerada")
    else:
        st.warning("Por favor, preencha todos os campos e envie a foto.")

