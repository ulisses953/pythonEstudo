# amostragem alatoria de 25% da base sem reposicao,
# com geracao de graficos de barra 

import random
import pandas as pd
import streamlit as st

print("Pegando os dados armazenados")
df = pd.read_csv("dados/Border_Crossing_Entry_Data.csv")

print("Gerando as amostra alatoria dos dados")
#gera valores aleatorios para a amostragem de 25% do dados
list_random_index = random.sample(
    range(int(df.index.min()), int(df.index.max()) + 1), int(df.index.max() * 0.25 ))

df_amostragem = df.loc[list_random_index]

print("Gerando pagina web")

st.set_page_config(page_title="Estatistica",layout="wide")
st.dataframe(df_amostragem)