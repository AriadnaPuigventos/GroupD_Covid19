'''
Date:201211
Funciones que correspondan a la visualización de los datos para la creación de dashboards, que se incluirán: gráficos, KPI's principales, ranking top 5 (lo + vendido, lo + visitado, etc).
Incluso añadir funciones que ayuden unir diferentes sources de una campaña: GA, AA, SM, Email, offline, etc.
'''
import pandas as pd #Instalado
import matplotlib.pyplot as plt #Instalado
import seaborn as sns #Instalado
from sklearn.preprocessing import LabelEncoder #Instalado


majors = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/world_marathon_majors.csv", sep = ";")
time_column = pd.to_timedelta(majors["time"].str.strip())
print(time_column)

def detect_outliers():
    #Detecting outliers about time because it exists much diference with de first and the last time.
    outliers = sns.boxplot(x = time_column.astype('timedelta64[s]'))
    print(outliers)
    Q1 = time_column.astype('timedelta64[s]').quantile(0.25)
    print(Q1)
    Q3 = time_column.astype('timedelta64[s]').quantile(0.75)
    print(Q3)
    IQR = Q3 - Q1
    print(IQR)

diccionario = dict(majors["country"].value_counts())
country_table = pd.DataFrame(diccionario, index = ["country"]).T
mylabels = country_table.index

def piechart_repitepais():
    #Get the proportion each item of the total pie chart.
    counts = []
    for value in diccionario.values():
        counts.append(value)
    print(counts)
    mylabels = country_table.index #str lista de países
    mysize = counts #int cantidad de veces que se repiten
    plt.pie(mysize, labels = mylabels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Countries")
    plt.axis('equal')
    plt.show()

dict1 = {"Country" : ['Kenya', 'United States', 'Ethiopia', 'Germany', 'United Kingdom', 'Japan', 'Norway', 'Canada', 'Portugal', 'Finland', 'Mexico', 'Russia', 'Poland', 'Brazil', 'Italy', 'New Zealand', 'Morocco', 'Belgium', 'South Africa', 'Tanzania', 'Australia', 'South Korea', 'Ireland', 'Latvia', 'Spain', 'Denmark', 'Colombia', 'Greece', 'Switzerland', 'Romania', 'Sweden', 'Yugoslavia', 'Hungary', 'China', 'Guatemala', 'Eritrea', 'Soviet Union'], "Counts" : [136, 104, 51, 36, 35, 22, 20, 17, 11, 10, 10, 8, 8, 7, 6, 5, 5, 5, 5, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]}
Countries = pd.DataFrame(dict1)

def Pie_Top10_Countries():
    # Firstly, it needs re-organizate the main dataframe and create a new one.
    Top_10_Countries = Countries[:10].copy()
    new_row = pd.DataFrame(data = {"Country" : ["Others"], "Counts" : [Countries["Counts"][10:].sum()]})
    Top_others = pd.concat([Top_10_Countries, new_row])
    # To create pie:
    fig1, ax1 = plt.subplots(figsize = (10,7))
    ax1.pie(Top_others["Counts"], labels = Top_others["Country"], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Countries Winners Marathon")
    ax1.axis('equal')
    plt.legend(Top_others["Country"], bbox_to_anchor=(1.10, 1), loc= 'upper left')
    plt.suptitle("Top 10 Countries", fontsize=12)
    plt.show()
    plt.savefig('Top_10_Countries.png')

def histogram_time():
    majors["time"] = pd.to_timedelta(majors["time"].str.strip())
    majors["time"] = majors["time"].astype('timedelta64[s]')
    majors["time"].hist(bins=5, legend="time", grid=False)
    plt.show()
    plt.savefig('Hist_time.png')

def histogram_year_time():
    print(majors.hist(bins=5))
    plt.show()
    plt.savefig('Hist_year_time.png')

def histogram_gender():
    majors["gender"] = majors["gender"].astype('category')
    print(majors["gender"].hist(bins=5, legend="Gender", grid=False))
    plt.show()
    plt.savefig('Hist_gender.png')

def histogram_country():
    majors.country = majors.country.astype('category')
    print(majors.country.hist(bins=5, legend="Countries", grid=False))
    print("Get better another argument to see almost it")

def histogram_countryby37bins():
    majors.country = majors.country.astype('category')
    graphic = majors["country"].hist(bins=36, legend="Countries", grid=False, figsize=(20, 5))
    plt.xticks(rotation='vertical')
    plt.show()
    plt.savefig('Hist_Countries.png')

def matrix():
    #To change type columns from object to encoding for showing a correlation matrix.
    majors['gender_1'] = majors['gender'].apply(lambda x: 0 if x == "Male" else 1)
    print(majors['gender_1'])
    majors["time"] = time_column.astype('timedelta64[s]')
    print(majors["time"])
    le = LabelEncoder()
    majors["encoded_country"] = le.fit_transform(majors["country"])
    print(majors["encoded_country"])
    majors["encoded_marathon"] = le.fit_transform(majors["marathon"])
    print(majors["encoded_marathon"])
    #To show the correlation Matrix with columns dataframe 1.
    plt.figure(figsize=(10,5))
    matrix = majors.corr()
    sns.heatmap(matrix, cmap="BrBG",annot=True)
    print(matrix)

def matrix_1960():
    majors['gender_1'] = majors['gender'].apply(lambda x: 0 if x == "Male" else 1)
    print(majors['gender_1'])
    majors["time"] = time_column.astype('timedelta64[s]')
    print(majors["time"])
    le = LabelEncoder()
    majors["encoded_country"] = le.fit_transform(majors["country"])
    print(majors["encoded_country"])
    majors["encoded_marathon"] = le.fit_transform(majors["marathon"])
    print(majors["encoded_marathon"])
    #To show the correlation Matrix from 1960 when Kenya was the first time compete in BWMM, almost in 1967 was the first woman who started to compete there as well.
    s_df = pd.DataFrame(majors[63:536])
    print(s_df)
    plt.figure(figsize=(10,5))
    matriz = s_df.corr()
    sns.heatmap(matriz, cmap="BrBG",annot=True)
    print(matriz)

# PIE CHART TIME SPENT HOURS
def time_spent():
    dict2 = {"Tasks": ["Searching datasets", "Path control", "Working in modules: functions, bucles...", "Wrangling Data: NaN, duplicates, outliers", "Visualization Data: graphics, boxplots", "Analyzing results", "Researching for value added"], "Hours": [32, 15, 72, 24, 192, 24, 12]}
    Tasks = pd.DataFrame(dict2)
    print(Tasks)
    Tasks.plot.pie(y='Hours', figsize=(5,5),labels=Tasks['Tasks'], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Time Spent")
    plt.legend(Tasks["Tasks"], bbox_to_anchor=(1.10, 1), loc= 'upper left')
    plt.suptitle("Main Tasks", fontsize=12)
    plt.show()
    plt.savefig('Pie_Time_Spent.png')


#Ideas Gráficos: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
import numpy as np


