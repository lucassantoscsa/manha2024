import streamlit as st
import datetime
import matplotlib.pyplot as plt

st.title("Manhã do Conhecimento CSA")
sono = st.time_input("Tempo de sono", value = datetime.time(0, 0))
tSono = sono.hour*60+sono.minute
tela = st.time_input("Tempo de tela", value = datetime.time(0, 0))
tTela = tela.hour*60+tela.minute
escola = st.time_input("Tempo de escola", value = datetime.time(0, 0))
tEscola = escola.hour*60+escola.minute
fisico = st.time_input("Tempo de Atividade Física", value = datetime.time(0, 0))
tFisico = fisico.hour*60+fisico.minute
tamanhos = [tSono, tEscola, tFisico, tTela]
soma = sum(tamanhos)
livre = 0
if soma < 24*60:
    col1, col2 = st.columns(2)
    with col1:   
        livre = 24*60-soma
        labels = 'Sono', 'Escola', 'Físico', 'Tela', 'Livre'
        sizes = [tSono, tEscola, tFisico, tTela,livre]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
else:
    col1, col2 = st.columns(2)
    with col1:
        st.title('Dia 1')
        tTelaAux = tTela
        tTela = 24*60-(soma-tTela)
        tTelaAux = tTelaAux-tTela
        labels = 'Sono', 'Escola', 'Físico', 'Tela'
        sizes = [tSono, tEscola, tFisico, tTela]
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig2)
    with col2:
        st.title('Dia 2')
        labels = '', 'Tela'
        sizes = [24*60-tTelaAux, tTelaAux]
        fig3, ax3 = plt.subplots()
        ax3.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig3)
