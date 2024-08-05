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

st.subheader("Avaliando o estudo na sala de aula", divider=True)
pontuacao_aluno = 0
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Sou pontual e frequente na escola.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Apresento facilidade de concentração durante a explicação dos professores.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Acompanho com atenção a correção dos exercícios.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Participo das aulas esclarecendo minhas dúvidas.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Tenho o hábito de realizar anotações sobre as aulas.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Escuto com atenção e respeito as dúvidas dos meus colegas.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Anoto os deveres e as datas das avaliações.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Durante as provas, consigo manter a calma.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Sinto-me respeitado(a) pelos meus colegas.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Sinto-me à vontade para solicitar ajuda aos meus professores.",
    options=opt,
))
st.subheader("Avaliando o estudo em casa", divider=True)
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Já organizei meu horário de estudos e consigo conciliar as tarefas escolares e as atividades extras (inglês, esportes, artes, lazer etc.).",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Em casa tenho um local de estudo silencioso e sem interferência de fatoresexternos (celular, TV, computador, animal de estimação, pessoas etc.).",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Realizo todas as atividades de “Para Casa” como um momento de estudo.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Realizo revisão da matéria dada.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Durante o estudo, consigo me concentrar.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Consigo estudar entre 1h e 1h30min sem interrupção.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Gosto de ler e escrever.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Tenho o hábito de ler informações e gêneros literários diversificados.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Sinto-me motivado para o estudo.",
    options=opt,
))
pontuacao_aluno = pontuacao_aluno + pont(st.select_slider("Acredito que sou capaz de aprender.",
options=opt,
))

with st.expander("Ver resultado"):
    if pontuacao_aluno <= 40:
        st.subheader("Sua pontuação é :red["+str(pontuacao_aluno)+"]", divider="red")
        st.text("Você precisa rever suas estratégias e se tornar mais comprometido(a). Afinal, você é o estudante, e a prática de estudos é sua responsabilidade. Se estiver precisando de ajuda, procure alguém e peça auxílio para mudanças de hábitos imediatamente. Você pode falar com seus pais, seu(sua) coordenador(a), seus professores e/ou o Setor de Psicologia Educacional.")
    with st.expander("Ver resultado"):
    elif pontuacao_aluno <= 60:
        st.subheader("Sua pontuação é :yellow["+str(pontuacao_aluno)+"]", divider="yellow")
        st.text("Apesar de já ter alguns hábitos saudáveis e adequados para uma rotina de estudos, alguns ajustes são necessários para que alcance seus objetivos. Por isso, verifique os itens que precisam ser aprimorados e os corrija o quanto antes. Se precisar de ajuda, você pode falar com seus pais, seu(sua) coordenador(a), seus professores e/ou o Setor de Psicologia Educacional.")
    else:
        st.subheader("Sua pontuação é :green["+str(pontuacao_aluno)+"]", divider="green")
        st.text("Você está no caminho certo! Continue comprometido(a) consigo mesmo e com seus estudos que o sucesso é garantido.")
    