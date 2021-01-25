'''
Date: 18/01/2021

'''
import os, sys, json
sys.path
import argparse
import pandas as pd

#from services.api.server import give_s

#This function and code has been made by Ariadna.

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--j", type=int, help="the information, insert 18", required=True)
args = vars(parser.parse_args())
print(args)
base = args["j"]

if base == 18:
    json_groupD = pd.read_json("http://0.0.0.0:6060/give_s?S=d102159467")
    print(json_groupD)
    """for i in range(1):
        path = os.path.dirname(path)
        sys.path.append(path)
        suerte = sys.path + os.sep + "api/t_d_averages.json"
        t_d_averages = read_json(fullpath=suerte)
        print(t_d_averages)"""
else:
    print("Try again, please")

#/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/GitHub_DS_ARIADNA/Project_EDA_CoronaVirus_Group_D/GroupD_Covid19/src/services/api/t_d_averages.json
#def json_df(x):
#print(json_df(x = base))

'''y = __file__
for i in range(2):
    y = os.path.dirname(y)
sys.path.append(y)
print(sys.path)
#settings_file = os.path.dirname(__file__) + "../../t_d_averages.json"
#t_d_averages = read_json(fullpath=settings_file)'''

"""y = __file__
for i in range(4):
    y = os.path.dirname(y)
sys.path.append(y)
print(sys.path)"""

'''def json_df(x):
    settings_file = os.path.dirname(__file__) + os.sep + "t_d_averages.json"
    t_d_averages = read_json(fullpath=settings_file)
    if base == 18:
        return t_d_averages
    else:
        print("Try again, please")
json_df(x = base)'''


'''def json_df():
    settings_file = os.path.dirname(__file__) + os.sep + "t_d_averages.json"
    t_d_averages = read_json(fullpath=settings_file)
    print(args)
    return t_d_averages
    #print("hola") if x == 18 else "Sorry, this is not the correct answer"


base = args["j"]
#print(json_df(x=base))'''