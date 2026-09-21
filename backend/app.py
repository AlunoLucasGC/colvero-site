#Importando Flask e renderizando arquivos HTML
from flask import Flask, render_template

#Criando a Aplicação
app= Flask(__name__)

#Criação da rota que representa a página inicial
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre ():
    return render_template("sobre.html")

@app.route("/contato", methods=["GET", "POST"])
def contato ():
    return render_template("contato.html")
    
#Inicia o servidor
if __name__ == "__main__": 
    app.run(debug = True) 