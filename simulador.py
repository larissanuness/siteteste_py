import streamlit as st 

#adc título da página
st.title("🕖 Simulador de Aposentadoria 📊")

nome = st.text_input('Nome:', placeholder="Insira seu nome completo.")
media_salarial = st.text_input('Contribuição Salarial:', placeholder="Insira o valor de contribuição.")

sexo = st.radio('Sexo:', ["Masculino", "Feminino"])

with st.sidebar:
    st.title('Dados:')

#    sexo = st.radio('Sexo:', ["Masculino", "Feminino"])

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

        
    tempo = st.slider('Tempo trabalhado:', 0, 70)

tempo_de_contribuicao = st.slider("Insira o tempo de contribuição:", 0,70)

if sexo == "Feminino":
    if tempo_de_contribuicao <= 29:
        st.write("Tempo mínimo de contribuição não atingido")
    



    

else:
    st.write("ok")

if st.button("Calcular"):   
   
   tempo_para_aposentar = int(idade * tempo ** (1/2))
   media_salarial = (media_salarial* 0,0) + (media_salarial * 0,2) * tempo


   if sexo == "Masculino":
       tempo_para_aposentar += 10

   
   
   st.write(f"Prezado(a) {nome}, faltam {tempo_para_aposentar} anos para você se aposentar. O salário da sua aposentadoria é {media_salarial}")


# alteração
