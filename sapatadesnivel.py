import streamlit as st
import numpy as np

# Cabeçalho com a imagem alinhada à esquerda e com tamanho ajustado para 30% da largura
st.image("Performance.jpg", use_column_width=False, width=300)  # Ajuste o width conforme necessário

st.title("Cálculo do Desnível Máximo entre Sapatas")
st.write(
    "Obtém o desnível máximo entre sapatas, de acordo com a NBR 6122:2022, com base no tipo de solo e distância entre sapatas")

# Dividir a página em duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    # Exibir a imagem na coluna da esquerda
    st.image("desnivel.jpg", caption="Esquema de desnível entre sapatas", use_column_width=True)

with col2:
    # Exibir os campos a serem preenchidos na coluna da direita
    inserir_manual = st.checkbox("Inserir ângulo manualmente")

    if inserir_manual:
        alpha = st.number_input("Insira o ângulo α (°):", min_value=1, max_value=89, value=45)
    else:
        # Escolha do tipo de solo
        tipo_solo = st.selectbox(
            "Selecione o tipo de solo:",
            ["Solos pouco resistentes (α = 60°)", "Solos resistentes (α = 45°)", "Rochas (α = 30°)"]
        )

        # Definição do ângulo α e cálculo de (90° - α)
        if "60°" in tipo_solo:
            alpha = 60
        elif "45°" in tipo_solo:
            alpha = 45
        else:
            alpha = 30

    beta = 90 - alpha  # Correção do ângulo

    # Entrada da distância entre sapatas
    distancia = st.number_input("Insira a distância entre as sapatas (m):", min_value=0.1, value=1.0)

    # Cálculo do desnível máximo usando 90° - α
    theta = np.radians(beta)  # Conversão para radianos
    desnivel_maximo = distancia * np.tan(theta)  # Correção na fórmula

    # Exibição do resultado
    st.write(f"### **Desnível máximo permitido:** {desnivel_maximo:.2f} m")

# Informação no final em tamanho pequeno
st.markdown('<p style="font-size: 10px; color: gray;">v 1.0.0<br>Autor: Luciano Pandolfi Hoffmann<br>'
            '<a href="https://www.performanceprotensao.com" target="_blank" style="font-size: 10px; color: gray;">www.performanceprotensao.com</a></p>',
            unsafe_allow_html=True)
