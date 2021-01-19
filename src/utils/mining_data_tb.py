'''
Date: 18/01/2021
Functionally about collect, clean and wrangling methods data.
'''
import pandas as pd

def countries(df):
    mask = df["location"] == "Venezuela" and "Spain"
    return mask
  