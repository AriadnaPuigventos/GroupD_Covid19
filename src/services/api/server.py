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
    return '{"clave":"valor", "clave_2":3}' #Aquí va nuestro json diccionario con el group_id y el token Dsum(ages)

@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['password']
    if x == "12345":
        return request.args
    else:
        return "No es el identificador correcto"

