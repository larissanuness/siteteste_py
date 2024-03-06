import streamlit as st

st.title("🕖 Simulador de Aposentadoria 📊")

nome = st.text_input('Nome:', placeholder="Insira seu nome completo.")
media_salarial = st.number_input('Contribuição Salarial:', 0, 10000000)
valor_salarial = int(media_salarial)

porcentagem1 = 0.6
porcentagem2 = 2/100
calculo = 0

sexo = st.radio('Sexo:', ["Masculino", "Feminino"])

with st.sidebar:
    st.title('Dados:')

    idade = st.slider('📆 Minha idade é:', 0, 100, 25)
    
    if idade < 18:
        st.write("👶")

    elif 18 < idade < 60:
        if sexo == "Masculino":
            st.write("🧔")
        
        else:
            st.write("👩")

    else:
        if sexo == "Masculino":
            st.write("👴")
        
        else:
            st.write("👩‍🦳")

    tempo_de_contribuicao = st.slider("Tempo de contribuição:", 0,70)
    tempo = int(tempo_de_contribuicao)

if sexo == "Feminino" and tempo_de_contribuicao >= 15:
        calculo = valor_salarial * porcentagem1
        
elif sexo == "Masculino" and tempo_de_contribuicao >= 20:
        calculo = valor_salarial * porcentagem1


botao_clicado = st.button("Calcular")
if botao_clicado:
    st.write(f"Prezado(a) {nome}, o salário da sua aposentadoria é {calculo:f}")

    
