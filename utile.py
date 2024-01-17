from streamlit import write
from googlesearcher import *
import googlesearcher
import inspect


def valid(a,b,d):
  if True:
    import textwrap



    text = ""
    text2 = ""

    for i in Google.search(a, num=str(d)):
      if b not in i.title or b == "" or b == " ":
        text += i.title if i.title != "" or i.title != " " else "aucune description trouvée ;("
        text += "  :  "
        text2 += "~"
        text2 += i.link
        text2 += "\n\n" 



    je = ""
    for i, o in zip(textwrap.wrap(text=text,width=500,break_long_words=False), text2.split("~")):
      je += i[:60 if len(i) > 60 else len(i)] + "..."if len(i) > 60 else " "
      je += "  :  "
      je += o
      je += "\n\n"


    print(je)
    return je

