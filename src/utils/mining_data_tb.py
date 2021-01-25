'''
Date: 18/01/2021
Functionally about collect, clean and wrangling methods data.
'''
import pandas as pd
import missingno as msno 

def countries(df):
    mask = df["location"] == "Venezuela" and "Spain"
    return mask

#Vizualitazion Correlation Matrix NaN's
def visual_NaNs():
    #msno.matrix()

#This function is to show GroupC's Data about Total Cases during 2020-21
def groupC_plot()
    grupoC = pd.read_json("http://apiprojectdata.ddns.net:5000/token:C98453658")
    grupoC = grupoC.dropna(how = "any")
    total_cases = grupoC.plot(figsize=(12,8))
    total_cases.set_xlabel("Date")
    total_cases.set_ylabel("Total Cases")
    total_cases.set_title("Json Group C")