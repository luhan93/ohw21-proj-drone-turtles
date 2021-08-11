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
                        "However, the major limiting factors is the human-power it takes to "
                        "label datasets of such size. With deep learning, the task of classification "
                        "can be automated with high accuracy. Here, we present results using YOLOv5 to "
                        "classify and localize turtles from drone images. The network is trained "
                        "with images from Nick Mortimer at CSIRO and we manually labelled 450 images using makesense.ai."
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

fileList = sorted(os.listdir("assets"))
fig_gt = px.imshow(io.imread(os.path.join("assets",fileList[2])), binary_backend="jpg")
fig_yolo = px.imshow(io.imread(os.path.join("assets",fileList[3])), binary_backend="jpg")
fig_simple = px.imshow(io.imread(os.path.join("assets",fileList[0])), binary_backend="png")
fig_adv = px.imshow(io.imread(os.path.join("assets",fileList[1])), binary_backend="png")

fig_gt.update_xaxes(showticklabels=False,showgrid=False)
fig_gt.update_yaxes(showticklabels=False,showgrid=False)
fig_yolo.update_xaxes(showticklabels=False,showgrid=False)
fig_yolo.update_yaxes(showticklabels=False,showgrid=False)
fig_simple.update_xaxes(showticklabels=False,showgrid=False)
fig_simple.update_yaxes(showticklabels=False,showgrid=False)
fig_adv.update_xaxes(showticklabels=False,showgrid=False)
fig_adv.update_yaxes(showticklabels=False,showgrid=False)

display_gt =  dbc.Card(
    id="display_gt",
    children=[
        dbc.CardHeader(html.H4("Manual Labels")),
        dbc.CardImg(src="/assets/val_batch0_labels.jpg", bottom=True),
        #dbc.CardFooter()
    ]
)

display_yolo =  dbc.Card(
    id="display_yolo",
    children=[
        dbc.CardHeader(html.H4("YOLOv5 Prediction")),
        dbc.CardImg(src="/assets/val_batch0_pred.jpg", bottom=True),
        #dbc.CardFooter()
    ]
)

display_vid = dbc.Card(
    id="display_vid",
    children=[
        dbc.CardHeader(html.H4("Happy Turtle Video")),
        dbc.CardBody(
            [
                html.Iframe(src='https://www.youtube.com/embed/VgZEfYVkSmw',
                            style={"height": "700px", "width": "100%"}),
            ]),
        #dbc.CardFooter()
    ]
)

display_ex_plot = html.Div(
                        [
                            html.Img(src="/assets/YoloExplain_2.png",
                                     style={ 'width':'80%'}),
                        ]),

display_ex_text = html.Div(
                        [
                            html.P(
                                "Object detection is a task in computer vision that involves identifying the presence, "
                                "location, and type of one or more objects in a given photograph."
                                "It is a challenging problem that involves building upon methods for object recognition "
                                "(e.g. where are they), object localization (e.g. what are their extent), and object "
                                "classification (e.g. what are they)."
                                "In recent years, deep learning techniques are achieving state-of-the-art results for "
                                "object detection, such as on standard benchmark datasets and in computer vision competitions. "
                                "YOLO originally started in 2016 up to v5 at the moment. "
                                "The approach involves a single convolutional neural network (CNN) that splits the input "
                                "into a grid of cells and each cell directly predicts a bounding box and object classification. "
                                "The result is a large number of candidate bounding boxes that are consolidated into a "
                                "final prediction by a post-processing step, using non-max suppression. "
                                "In this project, we implemented YOLOv5 in Pytorch, trained the model with 450 drone "
                                "taken turtle images, and successfully detected the turtle in a drone taken video."

                            ),
                        ], style={ 'fontSize': 12}),


display_ex = dbc.Card(
    id="display_ex",
    children=[
        dbc.CardHeader(html.H4("YOLO (You Only Look Once)")),
        dbc.CardImg(src="/assets/yoloex.png", bottom=True),
        dbc.CardBody(
            display_ex_text
            ),
    ]
)
app.layout = html.Div(
    [jumbotron,
    dbc.Row([
             display_ex
         ], style={'marginTop': 20,'marginLeft': 20,'marginRight': 20}, justify="center"),
    dbc.Row([
         dbc.Col(
             html.Div(id="left_column",
                      children = [
                        display_gt
                          #html.Img(src=app.get_asset_url('val_batch0_labels.jpg')),
                      ],style={'marginTop': 20,'marginLeft': 20}),width={'size':6}),
         dbc.Col(
             [html.Div(id="right_column",
                       children = [
                           display_yolo,
                       ],style={'marginTop': 20,'marginRight': 20}),

              ]
             ,width={'size':6}
         )]),
     dbc.Row([
           dbc.Col(html.Div(id="video",
                      children = [
                        display_vid
                          #html.Img(src=app.get_asset_url('val_batch0_labels.jpg')),
                      ],style={'marginTop': 20,'marginLeft': 20,'marginRight': 20}),width={'size':12})
     ], style={'marginTop': 20},justify="center",),

    # dbc.Row([
    #             dbc.Col(display_ex_simple,width=4),
    #             dbc.Col(display_ex_adv,width=8),
    #         ], style={'marginTop': 20},justify="center"),


     ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

