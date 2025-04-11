# 3_Gerenciar_Usuarios.py

import streamlit as st
import json
from utils.layout import cabecalho_pag, rodape
from utils.auth import carregar_usuarios, salvar_usuarios

cabecalho_pag("Gerenciar Usuários")

usuarios = carregar_usuarios()

for usuario in usuarios:
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**Nome:** {usuario['nome']}")
        st.write(f"**E-mail:** {usuario['email']}")
        st.write(f"**Tipo:** {'Admin' if usuario['tipo'] == 'admin' else 'Aluno'}")
        st.write(f"**Status:** {'Aprovado' if usuario['aprovado'] else 'Pendente'}")
    with col2:
        if usuario['tipo'] != 'admin':
            if st.button("Aprovar", key=f"aprovar_{usuario['usuario']}"):
                usuario['aprovado'] = True
                salvar_usuarios(usuarios)
                st.success("Usuário aprovado.")
            if st.button("Excluir", key=f"excluir_{usuario['usuario']}"):
                usuarios.remove(usuario)
                salvar_usuarios(usuarios)
                st.warning("Usuário excluído.")
rodape()
