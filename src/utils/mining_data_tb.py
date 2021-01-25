'''
Date: 18/01/2021
Functionally about collect, clean and wrangling methods data.
'''
import pandas as pd
import missingno as msno

def date( column):
    column= pd.to_datetime(column)

def countries(df, code):
    mask = df[df["iso_code"]==code]
    return mask

def column_erraser(df, col1=None, col2=None,col3=None,col4=None,col5=None, col6=None, col7=None, col8=None, col9=None, col10=None):
    name = df.drop(df.columns.difference([col1, col2,col3,col4,col5, col6, col7, col8, col9, col10]), 1)
    return name

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return list(pairs_to_drop)

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

def A_4_b(df, column, key, freq):
    df[column] = pd.to_datetime(df[column])
    name =df.groupby(pd.Grouper(key= key , freq= freq )).sum()
    return name

