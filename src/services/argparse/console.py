'''
Date: 18/01/2021

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

