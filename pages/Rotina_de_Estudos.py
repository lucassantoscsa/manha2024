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
    return(q)

st.header("Avaliando o estudo na sala de aula", divider=True)
pont(st.select_slider(
    "Sou pontual e frequente na escola?",
    options=opt,
))
st.header(pont)
