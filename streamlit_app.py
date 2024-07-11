import streamlit as st
import datetime
import matplotlib.pyplot as plt

st.title("🎈 **My new a**pp po")
sono = st.time_input("Tempo de sono", value = datetime.time(0, 0))
tSono = sono.hour*60+sono.minute
tela = st.time_input("Tempo de tela", value = datetime.time(0, 0))
tTela = tela.hour*60+tela.minute
escola = st.time_input("Tempo de escola", value = datetime.time(0, 0))
tEscola = escola.hour*60+escola.minute
fisico = st.time_input("Tempo de Atividade Física", value = datetime.time(0, 0))
tFisico = fisico.hour*60+fisico.minute
soma = 

labels = 'Sono', 'Escola', 'Físico', 'Tela'
sizes = [tSono, tEscola, tFisico, tTela]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=false, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
