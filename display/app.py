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
import os
from skimage import io

app = dash.Dash(name='app',  external_stylesheets=[dbc.themes.FLATLY])
server = app.server


jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H1("TURTLE DETECTION USING DEEP LEARNING", className="display-5"),
                html.P(
                    "Johnathan Evanilla, Lu Han, Alex Kerney, Daria Micovic, Alejandra Ortiz, Yelena Randall, Camille Ross, Dwight Sablan, John Stanco",
                    className="lead",
                ),
                html.Div(
                    [
                        html.P(
            "Thanks to technical advancements in drones and autonomous underwater vehicles, "
			"we are now able to capture large amounts of data from marine environments. "
			"However, on eof the major limiting factors is the human-power it takes to "
			"label datasets of such size. With deep learning, the task of classification "
			"can be automated with high accuracy. Here, we present results using YOLOv5 to "
			"classify turtles, sharks and dolphins from drone images. The network is trained "
			"with images from Nick Mortimer at CSIRO and we manually labelled 450 images using makesense.ai. The labels "
			"are in the form of bounding boxes around target species defined by expert analysts."
                        ),
                    ], style={'marginBottom': -60, 'marginTop': -10, 'fontSize': 12})
                ]
        )
                    ],className="bg-primary text-white",style={'marginBottom': 5,'marginTop':-50}
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

fileList = os.listdir("assets")
fig_gt = px.imshow(io.imread(os.path.join("assets",fileList[0])), binary_backend="jpg")
fig_yolo = px.imshow(io.imread(os.path.join("assets",fileList[1])), binary_backend="jpg")

display_gt =  dbc.Card(
    id="display_gt",
    children=[
<<<<<<< HEAD
        dbc.CardHeader(html.H4("Manual Labels")),
=======
        dbc.CardHeader(html.H4("Ground truth")),
>>>>>>> 8991bbd23bc741152bfacd2075cc3852d8ac95e2
        dbc.CardBody(
            [
                dcc.Graph(id="gt",
                figure = fig_gt),
            ]),
        #dbc.CardFooter()
    ]
)

display_yolo =  dbc.Card(
    id="display_yolo",
    children=[
        dbc.CardHeader(html.H4("YOLOv5 Prediction")),
        dbc.CardBody(
            [
                dcc.Graph(id="yolo",
                figure = fig_yolo),
            ]),
        #dbc.CardFooter()
    ]
)

display_vid = dbc.Card(
    id="display_vid",
    children=[
        dbc.CardHeader(html.H4("Results")),
        dbc.CardBody(
            [
<<<<<<< HEAD
                html.Iframe(src='https://www.youtube.com/embed/VgZEfYVkSmw', width = 900, height = 500),
=======
                html.Iframe(src='https://www.youtube.com/embed/VgZEfYVkSmw', width = 500, height= 500),
>>>>>>> 8991bbd23bc741152bfacd2075cc3852d8ac95e2
            ]),
        #dbc.CardFooter()
    ]
)
app.layout = html.Div(
    [jumbotron,
     dbc.Row([
         dbc.Col(
             html.Div(id="left_column",
                      children = [
                        display_gt
                          #html.Img(src=app.get_asset_url('val_batch0_labels.jpg')),
                      ]),width={'size':6}),
         dbc.Col(
             [html.Div(id="right_column",
                       children = [
                           display_yolo,
                       ]),

              ]
             ,width={'size':6}
         )]),
     dbc.Row([
            display_vid,
     ], style={'marginTop': 20},justify="center",)



     ]
)


if __name__ == "__main__":
    app.run_server(debug=False)

