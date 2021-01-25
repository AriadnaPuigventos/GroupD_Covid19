'''
Date: 18/01/2021

'''

from flask import Flask, request, render_template
import json
import os
import pandas as pd

#We couldn't import this function so we prefer copy it here directly:

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed


# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------

#We made this f() Xeles and Ariadna with the Gabriel's help in a tutor.
@app.route('/')
def give_default():
    return "Start the adventure!"

#These functions have done by Javi Gil. 
@app.route('/give_n', methods=['GET'])
def give_n():
    N = request.args['N']
    if N == "d104":
        return "For the next step you need -->  d102159467"
    else:
        return "Don't know our ages, don't believe!!"

@app.route('/give_s', methods=['GET'])
def give_s():
    settings_file = os.path.dirname(__file__) + os.sep + "t_d_averages.json"
    t_d_averages = read_json(fullpath=settings_file)
    S = request.args['S']
    if S == "d102159467":
        return t_d_averages 
    else:
        return "I am affraid not, try again"
    
#We made this f() Xeles and Ariadna with the Gabriel's help in a tutor.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6060)