from flask import Flask
from flask import render_template

import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb
from flask import request
import urllib
Dados = pd.read_excel('C:/aula8/PesquisaAuto.xlsx', 'Pesquisa')





Mplt.hist(Dados["Imagem"], bins=5)
Mplt.savefig("static\Grafico2.JPG")

sb.jointplot(x="Preco", y="Imagem",  data=Dados)
Mplt.savefig('site\Grafico.JPG')




App = Flask(__name__,  static_folder='site', static_url_path='')

@App.route("/", methods=["GET"])
@App.route("/dispersao", methods=["GET"])
def Home():
    idgrafico = request.args['id']   
    return render_template ("index.html",Nome=idgrafico)

@App.route("/histograma", methods=["GET"])
def Contato():
    idgrafico = request.args['id']   
    return render_template ("histograma.html", Nome=idgrafico)


@App.route("/lira", methods=["GET"])
def Contato2():
  return render_template ("histograma.html")




if __name__ == "__main__":
    App.run(port=80, debug=True)
