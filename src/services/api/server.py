'''
Date: 18/01/2021

'''

from flask import Flask, request, render_template
import json
import os

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route('/')
def give_default():
    return "hola"

@app.route('/give_n', methods=['GET'])
def give_n():
    N = request.args['N']
    if N == "d104":
        return "For the next step you need -->  d102159467"
    else:
        return "No os sabeis nuestros cumpleaños"

@app.route('/give_s', methods=['GET'])
def give_s():
    settings_file = os.path.dirname(__file__) + os.sep + "t_d_averages.json"
    t_d_averages = read_json(fullpath=settings_file)
    S = request.args['S']
    if S == "d102159467":
        return t_d_averages 
    else:
        return "I am affarid not, try again"
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6060)