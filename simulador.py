import streamlit as st

st.title("🕖 Simulador de Aposentadoria 📊")

nome = st.text_input('Nome:', placeholder="Insira seu nome completo.")
media_salarial = st.number_input('Média Salarial:', 0, 10000000)
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
tempo_h = 20
tempo_f = 15
tempo_limite_h = tempo - tempo_h
tempo_limite_f = tempo - tempo_f



botao_clicado = st.button("Calcular")
if botao_clicado:

    if sexo == "Feminino":
                    
            if idade < 58:
                st.write("Idade mínima não atingida.")

            elif tempo_de_contribuicao < 15:
                st.write("Tempo de contribuição não atingido.")
            else:
                calculo = (media_salarial * porcentagem1) + ((media_salarial * porcentagem2) * tempo_limite_f)
                st.write (f"Prezada {nome} valor da sua aposentadoria será {calculo}")

    if sexo == "Masculino":
        if idade < 60:
            st.write("Idade mínima não atingida.")
        elif tempo_de_contribuicao < 20: 
            st.write("Tempo de contribuição não atingido.")
        else:
            calculo = (media_salarial * porcentagem1) + ((media_salarial * porcentagem2) * tempo_limite_h)
            st.write (f"Prezado {nome} valor da sua aposentadoria será {calculo}")
    


