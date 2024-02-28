import streamlit as st
from utile import valid

import googlesearch

try:
  from googlesearch import Search
  
except Exception:
  st.write(dir(googlesearch))



def b():
  st.balloons()
  st.snow()

number = st.slider(min_value=1, max_value=100, step=1, label="entrez le nombre de recherches a effectué")
mots = st.text_area("entrez les mots a rechercher")
ban_words = st.text_area("entrez les mots ne devant pas figurer dans les recherches (faite attention a ne pas avoir appuyé sur entrée !)")

extent = st.selectbox("choisisez l'extension : ", [
    ".com",
    ".org",
    ".net",
    ".de",
    ".uk",
    ".in",
    ".br",
    ".fr",
    ".jp",
    "toute extensions"
])

st.button("quelque chose de fun .", on_click=lambda:st.balloons())
st.button("autre chose de fun .", on_click=lambda:st.snow())
st.button("derniere chose de fun .", on_click=lambda:b())
x = st.button("entrez .")
st2 = st.container()

a = valid(mots, ban_words, number, extent).split("+++++++")
try:
  st.write(a[1])
except Exception:
  pass

a = a[0].split("+++++++")

if x:
  for i in a:
      st2.write(i)

