from streamlit import write
from googlesearcher import *
import inspect



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
    return text



