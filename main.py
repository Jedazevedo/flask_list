from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Area():
    def __init__(self, nome, area, perimetro, potencia_luz):
        self.nome = nome
        self.area = area
        self.perimetro = perimetro
        self.potencia_luz = potencia_luz
            
lista =[]

@app.route('/')
def inicio():
    return render_template('index.html', 
                           titulo='Dependências',
                           areas = lista)

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    area = request.form['area']
    perimetro = request.form['perimetro']
    
    area = float(area)
    perimetro = float(perimetro)
    
    if area <=6: 
        potencia_iluminacao = 100
    elif area <=10:
        potencia_iluminacao = 160
    elif area <=14:
        potencia_iluminacao = 220
    elif area <=18:
        potencia_iluminacao = 280
    elif area <=22:
        potencia_iluminacao = 340

    area = Area(nome, area, perimetro, potencia_iluminacao)
    lista.append(area)
    return redirect('/')


app.run(debug=True)