from flask import Flask
from flask import render_template

import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb
from flask import request
import urllib
import random
Dados = pd.read_excel('C:/aula8/PesquisaAuto.xlsx', 'Pesquisa')


import random




#Mplt.hist(Dados["Imagem"], bins=5)
#Mplt.savefig("static\Grafico2.png")

#sb.jointplot(x="Preco", y="Imagem",  data=Dados)
#Mplt.savefig('site\Grafico.png')




App = Flask(__name__,  static_folder='site', static_url_path='')

@App.route("/", methods=["GET"])
@App.route("/dispersao", methods=["GET"])
def Home():

  for x in range(10):
   valor =  random.randint(1,2000)   


   idgrafico = request.args.get("id", 0, type=int)

   if idgrafico == 0:
        return render_template ("index.html")
   else:
        if idgrafico == 1: #BOX-PLOT
           
             #criar regra no js para esse grafico apenas 1 coluna.             
                           
            sb.boxplot(y="Imagem", data=Dados)         
            #Mplt.savefig("site\img" + str(idgrafico) + str(valor) +".png") 
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()            
            #return render_template ("index.html",Nome="img" +  str(idgrafico) + str(valor) +".png?valor="+str(valor))   
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))   
        

        if idgrafico == 2: #HISTOGRAMA COM DENSIDADE
             #criar regra no js para esse grafico apenas 1 coluna.
                           
            sb.distplot(Dados["Imagem"], bins=10, kde=True)           
            #Mplt.savefig("site\img" + str(idgrafico) + str(valor) +".png")
            Mplt.savefig("site\graficonovo.png")
            Mplt.clf()              
            return render_template ("index.html",Nome="graficonovo.png?valor="+str(valor))   
        
        else:
            return render_template ("index.html",Nome=idgrafico)           


@App.route("/histograma", methods=["GET"])
def Contato():

 
   idgrafico = request.args.get("id", 0, type=int)    
   return render_template ("histograma.html",Nome=idgrafico)
  




@App.route("/lira", methods=["GET"])
def Contato2():
  return render_template ("histograma.html")




if __name__ == "__main__":
    App.run(port=80, debug=True)
