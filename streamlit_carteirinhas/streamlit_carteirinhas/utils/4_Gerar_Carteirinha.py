# 4_Gerar_Carteirinha.py

import streamlit as st
from utils.auth import usuario_autenticado, carregar_usuarios
from utils.gerar_carteirinha import gerar_imagem_carteirinha
from utils.layout import cabecalho_pag, rodape
import os

cabecalho_pag("Gerar Carteirinha")

usuario = usuario_autenticado()

if usuario:
    if usuario.get("aprovado"):
        st.success("Cadastro aprovado. Gere sua carteirinha.")
        imagem_path = gerar_imagem_carteirinha(usuario)
        if imagem_path and os.path.exists(imagem_path):
            st.image(imagem_path, caption="Sua carteirinha gerada", use_column_width=True)
            with open(imagem_path, "rb") as file:
                btn = st.download_button("📥 Baixar Carteirinha", data=file, file_name="carteirinha.png", mime="image/png")
        else:
            st.warning("Não foi possível gerar a carteirinha.")
    else:
        st.warning("Aguardando aprovação do administrador.")
else:
    st.warning("Você precisa estar logado para acessar.")
rodape()
