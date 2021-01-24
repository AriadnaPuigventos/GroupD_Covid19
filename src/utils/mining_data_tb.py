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