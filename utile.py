from streamlit import write
from googlesearcher import *
import inspect

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
    answer = answer_element

  return answer

def valid(a, b, d, c):
  if True:
    import textwrap



    text = ""


    for i in Google.search(a, num=str(d)):
      if i.title is not None and i.link is not None:
        if (b.strip() not in i.title and (b != "" or b != " ")) or b == "" or b == " ":
          if (c in i.link or c == "toute extensions"):
            text += i.title if i.title != "" or i.title != " " else "aucune description trouvée ;("
            text += "  :  "
            text += "\n\n"
            text += i.link
            text += "\n\n" 
            text += "+++++++"



    #je = ""
    #for i, o in zip(textwrap.wrap(text=text,width=500,break_long_words=False), text2.split("~")):
    #  je += i[:60 if len(i) > 60 else len(i)] + "..."if len(i) > 60 else " "
    #  je += "  :  "
    #  je += o
    #  je += "\n\n"
#
#
#
    if answer(a) != None:
      return text #(text, answer(a))
    else :
      return text #(text)
