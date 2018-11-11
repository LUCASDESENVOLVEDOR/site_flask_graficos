from flask import Flask
from flask import render_template

import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb
from flask import request
import urllib
import random
Dados = pd.read_excel('PesquisaAuto.xlsx', 'Pesquisa')



App = Flask(__name__,  static_folder='site', static_url_path='')

@App.route("/", methods=["GET"])
@App.route("/dispersao", methods=["GET"])
def Home():

  for x in range(10):
   valor =  random.randint(1,2000)   

   idgrafico = request.args.get("id", 0, type=int)
   var1 = request.args.get("var1", 0, type=int)
   var2 = request.args.get("var2", 0, type=int)


   if idgrafico == 0:
        return render_template ("index.html")
   else:
        if idgrafico == 1: #BOX-PLOT
            coluna = nomedacoluna(var1)                            
            sb.boxplot(y=coluna, data=Dados) 
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))  
        if idgrafico == 2: #HISTOGRAMA COM DENSIDADE                        
            coluna = nomedacoluna(var1)   
            sb.distplot(Dados[coluna], bins=10, kde=True) 
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()              
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))  
        if idgrafico == 3: #BARRAS COM MÉDIAS            
            coluna = nomedacoluna(var1)   
            coluna2 = nomedacoluna(var2)                
            sb.barplot(x=coluna, y=coluna2, data=Dados)
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()              
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))  
        if idgrafico == 4: #BOX-PLOT CATEGORIZADO
            coluna = nomedacoluna(var1)   
            coluna2 = nomedacoluna(var2) 
            sb.boxplot(x=coluna, y=coluna2, data=Dados) 
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()              
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))
        if idgrafico == 5: #Dispersão com densidade
            coluna = nomedacoluna(var1)   
            coluna2 = nomedacoluna(var2)           
            sb.kdeplot(Dados[coluna], Dados[coluna2])          
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()              
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))  
        
        else:
            return render_template ("index.html",Nome=idgrafico)           




def nomedacoluna(argument):

    #return "Imagem"


    if (argument == 1):
      return "Respondente"

    if (argument == 2):
      return "Imagem"

    if (argument == 3):
      return "Utilitario"

    if (argument == 4):
      return "Preco"

    if (argument == 5):
      return "Genero"

    if (argument == 6):
      return "Idade"

    if (argument == 7):
      return "Filhos"

    if (argument == 8):
      return "Renda"

       
    if (argument == 9):
      return "Pequeno"

    if (argument == 10):
      return "Prototipo"

    
    if (argument == 11):
      return "EstadoCivil"
   


if __name__ == "__main__":
    App.run(port=80, debug=True)
