from flask import Flask, render_template, request, redirect
import math
app = Flask(__name__)

class Area():
    def __init__(self,
                 nome: str,
                 area: float,
                 perimetro: float,
                 potencia_luz: int, 
                 quantidade_tugs: int):
        self.nome = nome
        self.area = area
        self.perimetro = perimetro
        self.potencia_luz = potencia_luz
        self.quantidade_tugs = quantidade_tugs
        
                
lista =[]
def potencia_iluminacao(area: float):
    if area<10: 
        potencia_luz = 100
    elif area<14:
        potencia_luz = 160
    elif area<18:
        potencia_luz = 220
    elif area <22:
        potencia_luz = 280
    elif area <26:
        potencia_luz = 340
    elif area <30:
        potencia_luz = 340
    else:
        potencia_luz = "alta"
    return potencia_luz    
def quantidade_tugs(area: float, perimetro: float):
    quantidade_de_tugs = 0
    if area<6:
        quantidade_de_tugs = 1        
    else:
        quantidade_de_tugs = math.ceil(perimetro/5)
    return quantidade_de_tugs   
 
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
    tugs = 0    

    area = Area(nome, area, perimetro, potencia_iluminacao(area), quantidade_tugs(area, perimetro))
    lista.append(area)
    return redirect('/')


app.run(debug=True)