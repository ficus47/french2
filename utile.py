from streamlit import write
from googlesearcher import *
import googlesearcher
import inspect


def valid(a,b,d):
  if True:
    import textwrap



    text = ""
    text2 = ""
    write(google.search(a, language="fr", number_of_results=d))
    for i in google.search(a, language="fr", number_of_results=d):
      if b not in i.description or b == "" or b == " ":
        text += i.description if i.description != "" or i.description != " " else "aucune description trouvée ;("
        text += "  :  "
        text2 += "~"
        text2 += i.url
        text2 += "\n\n" 



    je = ""
    for i, o in zip(textwrap.wrap(text=text,width=500,break_long_words=False), text2.split("~")):
      je += i[:60 if len(i) > 60 else len(i)] + "..."if len(i) > 60 else " "
      je += "  :  "
      je += o
      je += "\n\n"


    print(je)
    return je

def valid(a,b,c):
  write(dir(googlesearcher))
