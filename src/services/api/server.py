'''
Date: 18/01/2021

'''

from flask import Flask, request, render_template
from utils.folders_tb import read_json
import os

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/c_json")
def create_json():
    return "t_d_averages.json"  #Aquí va nuestro json diccionario con el group_id y el token Dsum(ages)

@app.route('/give_me_id', methods=['GET'])
def give_id():
    N = request.args['N']
    if N == "d104":
        S = request.args['S']
        if S == "d102159467"
            return "C:\Users\javig\OneDrive\Documents\Bootcamp\Proyecto_EDA_GroupD\GroupD_Covid19\notebooks\t_d_averages.json"
    else:
        return "No es el identificador correcto"

