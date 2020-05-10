# -*- coding: utf-8 -*-
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# from app import app

####### NavBar #######
navbar = dbc.NavbarSimple(
    children=[
        html.Span(
            [
                html.A(
                    html.I(className = "fa-3x fab fa-github", style={'color':'#ffffff'}),
                href = "https://github.com/dkedar7/Data-Analyzer", target="_blank",
                className="mx-3"
                    ),
                    html.A(
                    html.I(className = "fa-3x fab fa-twitter-square", style={'color':'#ffffff'}),
                href = "https://www.twitter.com/dkedar7/", target="_blank",
                className="mx-3"
                    ),
                    html.A(
                    html.I(className = "fa-3x fab fa-linkedin", style={'color':'#ffffff'}),
                href = "https://www.linkedin.com/in/dkedar7/", target="_blank",
                className="mx-3"
                    )
            ]
        ),
    ],
    brand="Data Analyzer",
    brand_href=None,
    color="#40587C",
    dark=True,
    brand_style = {"font-size":"200%"},
    style = {"padding":"2% 0% 0% 0%"}
)

####### Header #######
header = dbc.Col([
            html.H1('Get an instant data analysis report of your spreadsheets', 
            style={'text-align':'center', "color":"white",
                "font-family": "Verdana; Gill Sans",
                "padding":"0% 0% 2% 0%", "font-size":"500%"}),
            html.H4('Using the powerful Pandas Profiling library on Python', 
            style={'text-align':'center', "color":"white",
                "font-family": "Verdana; Gill Sans","font-size":"200%"})
            ],
            style ={"padding":"5% 2% 5% 2%", "background-color":"#40587C"}
            )

####### Collapse button #######
collapse_button = dbc.Row(
    dbc.Button(
            "Learn how",
            id="collapse-button",
            className="mb-3",
            color="primary",
            style = {"font-size":"250%"}
        ),
        justify = 'center', style ={"background-color":"#40587C"}
)

steps = ["Step 1. Click on the 'Select Spreadsheet' button to upload a .xlsx, .xls or a .csv spreadsheet",
html.Br(),
"Step 2. If you upload a .xlsx or .xls spreadsheet, the app will ask you which sheet you want to analyze",
html.Br(),
"Step 3. Select 'Skip rows' - How many rows from the top the app should skip to read the actual table",
html.Br(),
'Step 4. Click on "Analyze"',
html.Br(),
"Step 5. Download the analysis as a .html report"]

collapse_card = dbc.Row(
    dbc.Collapse(
            dbc.Card(dbc.CardBody(steps, style = {"font-size":"150%"})),
            id="collapse",
                ),
        justify = 'center'
)

####### Upload button #######
upload_button = dbc.Col([
                dcc.Upload(
        id='upload-data',
        children=dbc.Col([
            html.A('Select spreadsheet',
            style = {"font-family": "Verdana; Gill Sans","font-size":"150%"})
        ]),
        style={
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
    ),
            ]
            )

####### Parameter control #######
parameters = [
    dbc.Row(
    [
        dbc.Col(
    [
        dbc.FormGroup(
            [
                html.Div(id="select-sheet-div",
                    children=
                    [
                        dbc.Label('Select sheet',style = {"font-size":"200%"}),
                        dcc.Dropdown(id="select-sheet",style = {"font-size":"130%"})
                    ],
                    style= {'display': 'none'}
                ),
                dbc.Label('Skip rows', style = {"font-size":"200%"}),
                dcc.Dropdown(id="skiprows",
                    options = [{"label" : rows, "value" : rows} for rows in range(1,11)],
                                value = 0, style = {"font-size":"130%"}
                            )
            ]
        )
    ]
        )
    ],
    justify = 'center'
),
dbc.Row(
    [
        dbc.Button("Analyze", id = 'analyze-button', size="md",
        color="primary", disabled = False,
        className = "mt-3 mx-auto",style = {"font-size":"200%"})
    ],
    justify = 'center'
),
dbc.Row(
    [
        dbc.Button("Download Report", id = 'download-button', size="md",
        color="primary", disabled = False,
        className = "mt-3 mr-3", href = "", external_link=True,style = {"font-size":"200%"})
    ],
    justify = 'center'
)
]
####### Analysis report iframe #######

spinner = dbc.Spinner(color="danger", id='spinner')

report_iframe = dbc.Col(id='output-report',
        style={'width': '80%',
            'height': '800px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }, loading_state = {'is_loading': True,
        'component_name':'spinner'})

####### Footer #######
footer = dbc.Row(
    [
        dbc.Col(
            [
                html.P(
                [
                    """
                    This application uses open-source work from 
                """,
                html.A(
                    html.U("Pandas Profiling"), 
                href = "https://github.com/pandas-profiling/pandas-profiling",
                target = "_blank",
                style = {"color":"white"}),
                """
                , a project to generate reports from Pandas dataframes.
                """
                ],
                style = {"color":"white","font-size":"120%"}
            )
            ],
            className="footer-disclaimer-content ",
            width=8,
        ),
        dbc.Col(
            [
                html.Span(
                    html.A(
                        html.I(className="fa-3x fab fa-github", style={"color":"#ffffff"}),
                        href="https://github.com/dkedar7/Data-Analyzer",
                        target = "_blank"
                    ),
                ),
                html.Span(
                    "   Copyright 2020", style={"color":"white"}
                ),
            ],
            width={"size" : 3, "offset":1}
        ),
    ],
    style ={"background-color":"#40587C", 
    "padding" : "2% 0% 0% 2%"}
)

####### Layout #######

layout = dbc.Container([
    dcc.Store(id='memory-output', storage_type='memory'),
    dbc.Row(
        [
            dbc.Col(
                [
                    navbar
                ]
            )
        ]
    ,style ={"background-color":"#40587C"}
    ),
    dbc.Row(
        [
            header
        ]
    ),
    collapse_button,
    collapse_card,
    dbc.Row(
        [
            upload_button
        ]
    ),
    dbc.Row(id="upload_intimation"),
    dbc.Container(
        parameters
    ),
    dbc.Row(
        [
            report_iframe
        ]
    ),
    footer
],
    fluid = True)