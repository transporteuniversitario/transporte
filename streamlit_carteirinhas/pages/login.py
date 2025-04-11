import streamlit as st
from utils.database import carregar_banco
import hashlib
from utils.layout import cabecalho_pag, rodape

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Login")

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

banco = carregar_banco()

with st.form("login_form"):
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    submit = st.form_submit_button("Entrar")

if submit:
    senha_cripto = hash_senha(senha)

    for user in banco["usuarios"]:
        if user["usuario"] == usuario and hash_senha(user["senha"]) == senha_cripto:
            st.success("Login realizado com sucesso como Administrador!")
            st.session_state.usuario = usuario
            st.session_state.tipo = "admin"
            st.switch_page("3_Gerenciar_Usuarios.py")

    for aluno in banco["alunos"]:
        if aluno["usuario"] == usuario and hash_senha(aluno["senha"]) == senha_cripto:
            if not aluno.get("autorizado", False):
                st.warning("Aguardando autorização do administrador.")
            else:
                st.success("Login realizado com sucesso como Aluno!")
                st.session_state.usuario = usuario
                st.session_state.tipo = "aluno"
                st.session_state.aluno = aluno
                st.switch_page("4_Gerar_Carteirinha.py")

    st.error("Credenciais inválidas. Verifique usuário e senha.")


cabecalho_pag("Login do Sistema")
# ... conteúdo da página ...
rodape()