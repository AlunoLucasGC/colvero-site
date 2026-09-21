#Importando Flask e renderizando arquivos HTML
from flask import Flask, render_template, request

#Criando a Aplicação
app= Flask(__name__)

#Criação das rotas que representam as páginas
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre ():
    return render_template("sobre.html")

@app.route("/contato", methods=["GET", "POST"])
def contato ():

        if request.method=="POST":
            nome=request.form["nome"]
            telefone=request.form["telefone"]
            mensagem=request.form["mensagem"]
            
            print(nome)
            print(telefone)
            print(mensagem) 
    
        return render_template("contato.html")
    
#Inicia o servidor
if __name__ == "__main__": 
    app.run(debug = True) 