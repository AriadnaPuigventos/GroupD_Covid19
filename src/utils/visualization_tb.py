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
    fig.show()
    plt.savefig()

def b_2_dots (df, x, y, title ):
    fig = px.scatter(df, x=x, y=y, title=title)
    fig.show()
    plt.savefig()

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
    plt.savefig()

def b_2_pie(df, column1, column2, title):
    pie= []
    pie.append(column1.mean())
    pie.append(column2.mean())
    fig = px.pie(df, values=pie, names=['new_cases','new_deaths' ], title=title)
    fig.show()
    

#Ideas Gráficos: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
import numpy as np


#This function is to show GroupC's Data about Total Cases during 2020-21
def groupC_plot(df):
    df = pd.read_json("http://apiprojectdata.ddns.net:5000/token:C98453658")
    grupoC = df.dropna(how = "any")
    total_cases = df.plot(figsize=(12,8))
    total_cases.set_xlabel("Date")
    total_cases.set_ylabel("Total Cases")
    total_cases.set_title("Json Group C")
    plt.show()
    plt.savefig('Total_Cases_GroupC')

def position(df, col1=None, col2=None, col3=None, col4=None, col5=None, col6=None, col7=None):
    df_posicion = df.groupby(col1).sum([col3, col4]).drop(df.columns.difference([col1, col2, col3, col4, col5, col6, col7]), 1)
    df_posicion_rank = df_posicion.rank().sort_values(by=[col3, col4], ascending=True)
    ven_rank = df_posicion_rank.loc["VEN"]
    esp_rank = df_posicion_rank.loc["ESP"]
    gbr_rank = df_posicion_rank.loc["GBR"]
    tur_rank = df_posicion_rank.loc["TUR"]
    prt_rank = df_posicion_rank.loc["PRT"]
    countries_d_ranking = pd.concat([ven_rank, esp_rank, gbr_rank, tur_rank, prt_rank])
    countries_d_ranking = pd.DataFrame([ven_rank, esp_rank, gbr_rank, tur_rank, prt_rank], columns=[col3, col4])
    countries_d_ranking = countries_d_ranking.astype(int)
    countries_d_ranking = countries_d_ranking.sort_values(by=col4)
    x = np.arange(len(countries_d_ranking.index))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots(figsize=(10, 10))
    rects1 = ax.bar(x - width/2, countries_d_ranking[col3], width, label='New Cases', color='b')
    rects2 = ax.bar(x + width/2, countries_d_ranking[col4], width, label='New Deaths', color='k')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Position')
    ax.set_title('Ranking Countries by General position')
    ax.set_xticks(x)
    ax.set_xticklabels(countries_d_ranking.index)
    ax.legend()
    plt.show()
    plt.savefig('Position_Countries')

def C10a(df):
    uk = df[df["iso_code"]=="GBR"]
    uk = uk.drop(uk.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    GBR = uk.dropna(how= "any", inplace = False)
    port = df[df["iso_code"]=="PRT"]
    port = port.drop(port.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    PRT = port.dropna(how= "any", inplace = False)
    turk = df[df["iso_code"]=="TUR"]
    turk = turk.drop(turk.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    TUR = turk.dropna(how= "any", inplace = False)
    esp = df[df["iso_code"]=="ESP"]
    esp = esp.drop(esp.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    ESP = esp.dropna(how= "any", inplace = False)
    ven = df[df["iso_code"]=="VEN"]
    ven = ven.drop(ven.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    VEN = ven.dropna(how= "any", inplace = False)
    df10 = pd.concat([GBR, PRT, TUR, ESP, VEN])
    df10.dropna(how="any", inplace=False)
    Countries5 = df10.groupby("iso_code").agg({"new_cases": [sum], "new_deaths": [sum], "total_cases": [max], "total_deaths": [max]})
    
    labels = Countries5.index
    total_cases = Countries5[( 'total_cases', 'max')]
    total_deaths = Countries5[('total_deaths', 'max')]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, total_cases, width, label='Total Cases', color="b")
    rects2 = ax.bar(x + width/2, total_deaths, width, label='Total Deaths', color="k")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Total')
    ax.set_title('Total cases and deaths by Countries')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.show()
    plt.savefig('Total_cases_deaths_by_countries')

def C10c(df):
    uk = df[df["iso_code"]=="GBR"]
    uk = uk.drop(uk.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    GBR = uk.dropna(how= "any", inplace = False)
    port = df[df["iso_code"]=="PRT"]
    port = port.drop(port.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    PRT = port.dropna(how= "any", inplace = False)
    turk = df[df["iso_code"]=="TUR"]
    turk = turk.drop(turk.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    TUR = turk.dropna(how= "any", inplace = False)
    esp = df[df["iso_code"]=="ESP"]
    esp = esp.drop(esp.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    ESP = esp.dropna(how= "any", inplace = False)
    ven = df[df["iso_code"]=="VEN"]
    ven = ven.drop(ven.columns.difference(["iso_code", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_deaths_per_million", "life_expectancy"]), 1)
    VEN = ven.dropna(how= "any", inplace = False)
    df10 = pd.concat([GBR, PRT, TUR, ESP, VEN])
    df10.dropna(how="any", inplace=False)
    Countries5 = df10.groupby("iso_code").agg({"new_cases": [sum], "new_deaths": [sum], "total_cases": [max], "total_deaths": [max]})
    sns.boxplot(x=Countries5[('total_deaths', 'max')])
    plt.show()
    plt.savefig('Outliers')

# df_posicion = df.groupby("iso_code").sum(["new_deaths", "new_cases"]).drop(world.columns.difference(["iso_code", "date", "new_cases", "new_deaths"]), 1)
# df_posicion_rank = df_posicion.rank().sort_values(by=["new_cases", "new_deaths"], ascending=True)