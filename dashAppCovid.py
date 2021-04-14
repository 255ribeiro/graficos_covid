import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import numpy as np
import pandas as pd

#import os
import zipfile
#from tensorflow.keras.utils import get_file



list_dia_semana = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']

# Load file
def load_dataset(fZipName):
    zf = zipfile.ZipFile('./data/' + fZipName + '.zip') 
    df = pd.read_csv(zf.open( fZipName + '.csv'), sep=';')

    # Prepoc datetime
    cat_dia_semana = pd.CategoricalDtype(categories= list_dia_semana , ordered=True)
    df['data'] = pd.to_datetime(df['data'],format="%Y-%m-%d")
    df['dia_semana'] = df['data'].dt.dayofweek
    df['dia_semana_nm'] = df['dia_semana'].replace({0:'seg', 1: 'ter', 2:'qua', 3:'qui', 4:'sex', 5:'sab', 6:'dom'}).astype(cat_dia_semana)
    return df

###

df = load_dataset('HIST_PAINEL_COVIDBR_13abr2021')


dictUfMuni = {}
for i in df['estado'].unique():
    fltr = df['estado'] == i
    df_UF = df.loc[fltr, :]
    #print(i)
    aux_list = []
    for j in df_UF['municipio'].unique():
        aux_list.append(j)
    dictUfMuni[i] = aux_list
estados = list(dictUfMuni.keys())

print(dictUfMuni)

app = dash.Dash()


app.layout = html.Div([
    dcc.Graph(id='casos_mm_fig'),
    dcc.Dropdown(id='uf_picker' ,
        options= [{'label': estado , 'value':  estado } for estado in estados ],
        value='BA'
        ),
    dcc.Dropdown(id='muni_picker', value = "Salvador")
])


@app.callback(
    dash.dependencies.Output('muni_picker', 'options'),
    [dash.dependencies.Input('uf_picker', 'value')]
)
def update_date_dropdown(uf):
    return [{'label': i, 'value': i} for i in dictUfMuni[uf]]



if __name__ == '__main__':
    app.run_server()