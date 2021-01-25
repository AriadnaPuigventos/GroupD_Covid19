import os
import os.path
#from src.utils.functions import 
import sys

""" Descargar el ultimo csv de la web. JAVI"""
def downloader():
    world = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', sep = ",")
    return world 


"""Funcion para añadir el path a la lista sys"""
"""hay que revisarla"""
def path_append(n):
    for i in range(n):
        x = os.path.dirname
        print(x)
    return sys.path.append(x)

"""Funcion para añadir el path a la lista sys"""
"""hay que revisarla"""
def path_append(n):
    path_list = []
    n = range(len(path_list))

    for i in path_list:
        x = os.path.dirname(i)
        print(x)
        path_list = sys.path.append(x)
        x = i + 1
    print(path_list)
    return path_list

""" Mask para valores raros del dataset de España"""
"""pensar si se pone, hay que revisarla"""
def mask_esp(col_name):
    esp[col_name] = esp[col_name].sort_values(by = [col_name]).drop.iloc[-1:-2, ]
    esp = esp.dropna(how = 'any', drop = True)
    esp = esp.reset_index(drop = True)
    return esp

""" Guardar varias figuras en un fichero PDF"""
def save_plot(fig, file):
    import matplotlib.backends.backend_pdf
    fig = []
    pdf = matplotlib.backends.backend_pdf.PdfPages(file)
    for f in fig:
        pdf.savefig()
        pdf.close()
    return pdf


""" Dataframe de columnas para analisis de tendencias"""

def countries_cols():
world = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    world = pd.read_csv("owid-covid-data.csv", sep = ",")
    world_cols = world.drop(world.columns.difference(['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','total_cases_per_million','new_cases_per_million','total_deaths_per_million', 'new_deaths_per_million','reproduction_rate', 'stringency_index']), 1)
 
    countries_list = ['ESP', 'GBR', 'PRT', 'TUR', 'VEN']

    countries_cols = world_cols[world_cols["iso_code"].isin(countries_list)]
    countries_cols.dropna(how = 'any', inplace = True)
    countries_cols.sort_values(by = ['date'], inplace=True)
    countries_cols['date'] = pd.to_datetime(countries_cols['date'])

    return countries_cols.reset_index(drop =True)

"""hay que revisarla"""
""" Extraccion de un dataset por pais"""

def countries(c, df):
    world = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', sep = ",")
    #world = pd.read_csv("owid-covid-data.csv", sep = ",")
    world_cols = world.drop(world.columns.difference((['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','total_cases_per_million','new_cases_per_million','total_deaths_per_million', 'new_deaths_per_million','reproduction_rate', 'stringency_index']), 1)
    #type(c) == str
    #c = c.upper()
    #countries_list = ['ESP', 'GBR', 'PRT', 'TUR', 'VEN']
    #acum = 0
    #for c in countries_list:
    df = world_cols[world_cols["iso_code"] == c ]
        #df = world_cols[world_cols["iso_code"].isin(countries_list)]
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values(by = ['date'], inplace=True)
    df.reset_index(drop=True)
        #acum +=1
    return df


""" Ploteo de una determinada columna de un dataframe con fechas en el eje X (columna 'date') 
en formato de linea"""

def graf_lines(df, col_name, colored, title):
    plt.plot("date", col_name, data = df, linestyle='solid', linewidth = 2, color= colored, label = title)

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(col_name)
    plt.legend()

    fig = plt.show()
    return fig

"""Ploteo de columnas para analisis de tendencias"""
def plot_cols_tend(df, col_name, title):
    fig = go.Figure(data=[go.Bar(x=df['date'], y=df[col_name])], layout_title_text= title)
    fig.show()
    return fig


"""hay que revisarla"""
""" Ploteo de una determinada columna de varios dataframe, con fechas en el eje X (columna 'date') 
en formato multilinea"""

def graf_multiple_lines(col_name, title, n, df, colored, labels):
    type(n) = int
    df = []
    range(len(df)) = n

    for i in df:
        plt.plot("date", col_name, data = df1, linestyle='solid', linewidth = 2, color= colored_1, label = labels)

    #col_name, title, df1, colored_1, df2, colored_2, df3, colored_3, df4, colored_4, df5, colored_5):
    #plt.plot("date", col_name, data = df1, linestyle='solid', linewidth = 2, color= colored_1, label = data)
    #plt.plot("date", col_name, data = df2, linestyle='solid', linewidth = 2, color= colored_2, label = title)
    #plt.plot("date", col_name, data = df3, linestyle='solid', linewidth = 2, color= colored_3, label = title)
    #plt.plot("date", col_name, data = df4, linestyle='solid', linewidth = 2, color= colored_4, label = title)
    #plt.plot("date", col_name, data = df5, linestyle='solid', linewidth = 2, color= colored_5, label = title)

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(col_name)
    plt.legend(label)

    fig = plt.show()
    return fig