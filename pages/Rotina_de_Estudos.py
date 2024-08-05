import streamlit as st
import datetime
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(
    page_title="Rotina de Estudos",
    page_icon="🔵",
)
st.image("https://www.colegiosantoantonio.com.br/wp-content/uploads/2024/06/csa-115-anos-1.png")
st.title("Manhã do Conhecimento CSA")
opt = [
        "Nunca",
        "Raramente",
        "Às vezes",
        "Quase sempre",
        "Sempre",
        
    ]
def pont(q):
    pontuacao = opt.index(q)+1
    return(pontuacao)

st.header("Avaliando o estudo na sala de aula", divider=True)
pontuacao_aluno = 0
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider(
    "Sou pontual e frequente na escola.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider(
    "Apresento facilidade de concentração durante a explicação dos professores.",
    options=opt,
))