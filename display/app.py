import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import flask

app = dash.Dash(name='app',  external_stylesheets=[dbc.themes.FLATLY])
server = app.server

jumbotron = dbc.Jumbotron(
    [
        html.H1("Turtle Detection using Deep Learning", className="display-3"),
        html.P(
            "Johnathan Evanilla, Lu Han, Alex Kerney, Daria Micovic, Alejandra Ortiz, Camille Ross, Dwight Sablan, John Stanco",
            className="lead",
        ),

        html.P(
            "The housing market in the U.S is blooming since last year. "
            "Due to Covid, the supply dropped as the demand rose. "
            "Home prices nationwide were up 26.3% year-over-year in May. "
            "At the same time, the number of homes sold rose 45.9% and the number of homes for sale fell 46.4%. "
            "New constructions can help close the nation's housing shortage. "
            "Number of new construction permits issued can serve as a indicator on the supply end. "
            "This dashboard provides some visualization on the amount of new construction permits in each month since 2004 in 50 states. "
        ),
        # html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ],className="bg-primary text-white"
)
species = ['turtle','shark','dolphin']
species_slt = html.Div(children=[
    html.Label(['Select a Species:'], style={'font-weight': 'bold', "text-align": "center"}),
    dcc.Dropdown(
        id='dropdown-dataset',
        options=[{"label": i.upper(),
                  "value": i}
                 for i in species],
        value='turtle',
        searchable=False,
        clearable=False,
    ),
],style={'marginLeft': 50,"width":"80%"}),


prev_next = html.Div(
    children=[
        dbc.ButtonGroup(
            style={"text-align": "center","width":"100%"},
            children=[
                dbc.Button(
                    "PREV",
                    color="secondary",
                    n_clicks=0,
                    id="prev",
                    outline=True,
                    active=False,
                    value = -1,
                ),
                dbc.Button(
                    "NEXT",
                    color="secondary",
                    n_clicks=0,
                    id="next",
                    outline=True,
                    active=False,
                    value = 1,
                ),
            ],
        ),
    ],style={'marginTop': 30}
)

rand = html.Div(
    children=[
        dbc.Button(
            "RANDOM",
            color="secondary",
            n_clicks=0,
            id="rand",
            outline=True,
            active=False,
            block=True
        )
    ],style={'marginTop': 30,"width":"80%"}
)

image_nav = dbc.Row(children=[
    dbc.Col(species_slt),
    dbc.Col(prev_next),
    dbc.Col(rand)
])

slider = html.Div(children=[
    html.Label(['Confidence Threshold:'], style={'font-weight': 'bold', "text-align": "center","width":"100%"}),
    dcc.Slider(
        id='threshold',
        min=0,
        max=1,
        step=0.05,
        value=0.3,
        marks={
            0: '0',
            0.5: '0.5',
            1: '1',

        },
        tooltip = { 'always_visible': True,
                    'placement':'bottom'}
    ),
],style={'marginLeft': 70,"width":"80%"}),

app.layout = html.Div(
    [jumbotron,
     dbc.Row([
         dbc.Col(
             html.Div(id="left_column",
                      children = [
                          dcc.Graph(id="human",
                                    figure = go.Figure()),
                          image_nav
                      ]),width={'size':6}),
         dbc.Col(
             [html.Div(id="right_column",
                       children = [
                           dcc.Graph(id="yolo",
                                     figure = go.Figure()
                                     ),
                           dbc.Row(slider)
                       ]),

              ]
             ,width={'size':6}
         )]),


     ]
)

if __name__ == "__main__":
    app.run_server(debug=True)