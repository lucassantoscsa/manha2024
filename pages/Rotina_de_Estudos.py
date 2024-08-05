import streamlit as st
import datetime
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(
    page_title="Tempo de Tela",
    page_icon="🔵",
)

q1 = st.select_slider(
    "Sou pontual e frequente na escola?",
    options=[
        "Nunca",
        "Raramente",
        "Às vezes",
        "Quase sempre",
        "Sempre",
        
    ],
)
st.write("My favorite color is", q1)