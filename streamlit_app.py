import streamlit as st
import datetime
import matplotlib.pyplot as plt
import numpy as np
st.image("https://www.colegiosantoantonio.com.br/wp-content/uploads/2024/06/csa-115-anos-1.png")
st.title("Manhã do Conhecimento CSA")
sono = st.time_input("Tempo de sono", value = datetime.time(0, 0))
tSono = sono.hour*60+sono.minute
escola = st.time_input("Tempo de escola", value = datetime.time(0, 0))
tEscola = escola.hour*60+escola.minute
estudos = st.time_input("Tempo de Estudos em Casa", value = datetime.time(0, 0))
testudo = estudos.hour*60+estudos.minute
fisico = st.time_input("Tempo de Atividade Física", value = datetime.time(0, 0))
tFisico = fisico.hour*60+fisico.minute
extra = st.time_input("Tempo de Atividades Extras", value = datetime.time(0, 0))
tExtra = extra.hour*60+extra.minute
refeicao = st.time_input("Tempo de Refeição e Higiente Pessoal", value = datetime.time(0, 0))
tRefeicao = refeicao.hour*60+refeicao.minute

with st.expander("Ver resultado"):
        tela = st.time_input("Tempo de uso do celular", value = datetime.time(0, 0))
        tTela = tela.hour*60+tela.minute
        tamanhos = [tSono, tEscola, tFisico,testudo, tTela,tExtra]
        soma = sum(tamanhos)
        livre = 0
        colors = plt.get_cmap('YlGnBu_r')(np.linspace(0.2, 0.7, len(tamanhos)+1))
        if soma < 24*60:
                livre = 24*60-soma
                labels = 'Sono', 'Escola', 'Atividades Físicas','Atividades Extras', 'Tela', 'Estudos', 'Refeição e Higiente Pessoal','Livre'
                sizes = [tSono, tEscola, tFisico, tExtra, tTela,testudo, tRefeicao, livre]                        
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, wedgeprops={"linewidth": 1, "edgecolor": "white","width":0.05},labels=labels, autopct='%1.1f%%', shadow=False, startangle=90,textprops={"color":"#31333f","fontsize":"large"})
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                fig1.set_facecolor('#ffffff')
                st.pyplot(fig1)
        else:
                
                tTelaAux = tTela
                tTela = 24*60-(soma-tTela)
                tTelaAux = tTelaAux-tTela
                labels = 'Sono', 'Escola', 'Atividades Físicas','Atividades Extras', 'Tela', 'Estudos', 'Refeição e Higiente Pessoal','Livre'
                sizes = [tSono, tEscola, tFisico, tExtra, tTela,testudo, tRefeicao, livre]  
                fig2, ax2 = plt.subplots()
                ax2.pie(sizes, wedgeprops={"linewidth": 1, "edgecolor": "white","width":0.05},labels=labels, autopct='%1.1f%%', shadow=False, startangle=90,textprops={"color":"#31333f","fontsize":"larger"})
                ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                fig2.set_facecolor('#ffffff')
                st.pyplot(fig2)
                horasNovo = round(tTelaAux/60)
                st.write("Com os dados apresentados, seria necessário mais um segundo dia em que você gastaria "+str(horasNovo)+" hora(s) usando o celular, será que você tem cumprido mesmo os horários que propôs acima? Veja abaixo quanto de um novo dia você gastaria.")                  
                labels = '', 'Tempo Excedente Gasto em Tela: '+str(horasNovo)+" horas."
                sizes = [24*60-tTelaAux, tTelaAux]
                fig3, ax3 = plt.subplots()
                ax3.pie(sizes, wedgeprops={"linewidth": 1, "edgecolor": "white","width":0.05},labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, textprops={"color":"#31333f","fontsize":"larger"})
                ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                fig3.set_facecolor('#ffffff')
                st.pyplot(fig3)
