'''
Date: 18/01/2021
This module are for function to open and read files
'''

import json #Instalado
import requests #Instalado
import pandas as pd #Instalado


def readcsv(ruta):
      df = pd.read_csv(ruta, sep = ",")
      return df

def downloader(df):
    world = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    return world 

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed