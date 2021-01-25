'''
Date:201211
Funciones que correspondan a la visualización de los datos para la creación de dashboards, que se incluirán: gráficos, KPI's principales, ranking top 5 (lo + vendido, lo + visitado, etc).
Incluso añadir funciones que ayuden unir diferentes sources de una campaña: GA, AA, SM, Email, offline, etc.
'''
import pandas as pd #Instalado
import matplotlib.pyplot as plt #Instalado
import seaborn as sns #Instalado
from sklearn.preprocessing import LabelEncoder #Instalado
import plotly.express as px
import plotly.graph_objects as go




def b_2_line(df, x, y, title ):
    fig=px.line(df, x= x, y= y, title= title)
    fig.update_xaxes(dtick="M1",tickformat="%b\n%Y")
    return fig.show()

def b_2_dots (df, x, y, title ):
    fig = px.scatter(df, x=x, y=y, title=title)
    return fig.show()

def b_2_bar(df, x, y, title ):
    fig=px.bar(df, x= x, y=y, title= title)
    fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
    fig.update_layout( autosize=False,
    width=5000,
    height=500,
    margin=dict(l=0, r=0, t=0, b=0))
    fig.show() 

#Ideas Gráficos: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
import numpy as np


