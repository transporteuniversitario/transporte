from PIL import Image, ImageDraw, ImageFont
import os

def gerar_carteirinha(dados, caminho_saida="static/carteirinhas", fundo_path="static/fundos/fundo_padrao.png"):
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)

    imagem_fundo = Image.open(fundo_path).convert("RGBA")
    draw = ImageDraw.Draw(imagem_fundo)

    fonte = ImageFont.truetype("static/fontes/arial.ttf", 28)

    draw.text((180, 100), f"Nome: {dados['nome']}", font=fonte, fill="black")
    draw.text((180, 140), f"Matrícula: {dados['matricula']}", font=fonte, fill="black")
    draw.text((180, 180), f"Curso: {dados['curso']}", font=fonte, fill="black")
    draw.text((180, 220), f"CPF: {dados['cpf']}", font=fonte, fill="black")
    draw.text((180, 260), f"Nascimento: {dados['data_nascimento']}", font=fonte, fill="black")
    draw.text((180, 300), f"Dias de Aula: {dados['dias_aula']}", font=fonte, fill="black")
    draw.text((180, 340), f"Validade: {dados['validade']}", font=fonte, fill="black")

    # Foto do aluno
    if dados.get("foto") and os.path.exists(dados["foto"]):
        foto = Image.open(dados["foto"]).resize((130, 130))
        imagem_fundo.paste(foto, (30, 100))

    # Assinatura
    if dados.get("assinatura") and os.path.exists(dados["assinatura"]):
        assinatura = Image.open(dados["assinatura"]).resize((120, 60))
        imagem_fundo.paste(assinatura, (180, 420))

    # Logos
    if dados.get("logo_prefeitura") and os.path.exists(dados["logo_prefeitura"]):
        logo1 = Image.open(dados["logo_prefeitura"]).resize((80, 80))
        imagem_fundo.paste(logo1, (600, 30))
    if dados.get("logo_secretaria") and os.path.exists(dados["logo_secretaria"]):
        logo2 = Image.open(dados["logo_secretaria"]).resize((80, 80))
        imagem_fundo.paste(logo2, (700, 30))

    caminho_imagem = os.path.join(caminho_saida, f"{dados['matricula']}.png")
    imagem_fundo.save(caminho_imagem)
    return caminho_imagem
