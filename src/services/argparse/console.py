'''
Date: 18/01/2021

'''
import sys
sys.path.append(x)
#/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/GitHub_DS_ARIADNA/Project_EDA_CoronaVirus_Group_D/GroupD_Covid19/src/services/argparse/console.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--j", type=int, help="the password, for correct answer insert 18", required=True)
args = vars(parser.parse_args())

def json_df(x):
    print(args)
    return t_d_averages
    #print("hola") if x == 18 else "Sorry, this is not the correct answer"


base = args["j"]
print(json_df(x=base))