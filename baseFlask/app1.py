from flask import Flask, render_template, request
from math import sqrt


app=Flask(__name__)

@app.route("/") #decorador o ruta
def index():
    titulo="Pagina de Inicio"
    listado = ['Python','Flask','Jinja2','HTML','CSS']
    return render_template("index.html", titulo=titulo,listado=listado)



@app.route("/operasbas", methods=["GET","POST"])
def operasbas():
    n1 = 0
    n2 = 0
    res = 0
    operacion = ''

    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        operacion = request.form.get('operacion')

        if operacion == 'sumar':
            res = float(n1) + float(n2)

        if operacion == 'restar':
            res = float(n1) - float(n2)

        if operacion == 'multiplicar':
            res = float(n1) * float(n2)

    return render_template("operasbas.html", n1=n1, n2=n2, res=res, operacion=operacion)

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    res = 0
    calcular = False

    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))

        res = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        calcular = True

    return render_template("distancia.html",x1=x1, y1=y1,x2=x2, y2=y2,res=res, calcular=calcular)


@app.route("/hola")
def hola():
    return "<h1> Hola PWA - IEVN1003</h1>"

#como pasar parametros por url

@app.route("/user/<string:nom>")
def user(nom):
    return "<h1>Hola User: {} </h1>".format(nom) #Para hacer perfomateo de una salida a pantalla

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "la suma es: {}".format(n1+n2)


if __name__=="__main__":
    app.run(debug=True)