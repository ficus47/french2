import streamlit as st
from utile import valid

import googlesearch

try:
  from googlesearch import Search
  
except Exception:
  st.write(dir(googlesearch))

from bs4 import BeautifulSoup
import requests

def answer(question):
  """
  Fonction qui répond à une question en utilisant Google Search.

  Args:
      question (str): La question à poser.

  Returns:
      str: La réponse à la question, ou None si aucune réponse n'est trouvée.
  """

  # Encodage de la question pour l'URL
  encoded_question = question.replace(" ", "+")

  # Requête HTTP vers Google Search
  url = f"https://www.google.com/search?q={encoded_question}"
  response = requests.get(url, headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
  "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.5,en;q=0.3",

})
  #print(response.text)

  # Analyse du code HTML de la page de résultats
  soup = BeautifulSoup(response.text, "html.parser")

  # Recherche de l'élément contenant la réponse
  answer_element = soup.find(class_="hgKElc")

  # Extraction du texte de la réponse
  try:
    answer = answer_element.text
  except Exception:
    answer = None

  return answer


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
st2 = st.container()


def clicker():
  if answer(mots) != None:
    st2.write(answer(mots))

  st2.write(valid(mots, ban_words, number, extent).split("+++++++"))


st2.button("entrez .", on_click=clicker())