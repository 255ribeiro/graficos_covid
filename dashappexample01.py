import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children =[
    html.H1('Dash Tutorials'),
    dcc.Graph(id = 'example1',
                figure = {
                            'data': [

                                {'x': [1,2,3,4,5], 'y': [6,7,8,4,3], 'type': 'bar', 'name': 'teste barplot'},
                                {'x': [1,2,3,4,5], 'y': [2,9,8,1,7], 'type': 'line', 'name': 'teste lineplot'}
                            ],

                'layout':{'title': 'Basic example'}

                })
])

if __name__ == '__main__':
    app.run_server(debug=True)
