'''
Date: 25/01/2021

'''
import os, sys, json
sys.path
import argparse
import pandas as pd
import numpy as np

# Javi & Ariadna - Master&Comanders vol.II

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--j", type=int, help="the information, insert 18", required=True)
args = vars(parser.parse_args())
print(args)
base = args["j"]

world_ = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
paises = ['GBR', 'PRT', 'VEN', 'TUR', 'ESP']
df = world_[world_["iso_code"].isin(paises)]
df = df.dropna(subset=["total_deaths"])
t_d_averages = df.groupby(by="date" ).agg({'total_deaths':'mean'})
t_d_averages= t_d_averages.reset_index()
t_d_averages['date'] = t_d_averages["date"].astype(str)
t_d_averages = t_d_averages.values.tolist()
jsonpaalex = {"t_d_averages":t_d_averages}
with open("t_d_averages.json", "w") as write_file:
    json.dump(jsonpaalex, write_file)

if base == 18:
   x = open("t_d_averages.json")
   data = json.load(x)
   print(data) 
else:
    print("Try again, please")



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