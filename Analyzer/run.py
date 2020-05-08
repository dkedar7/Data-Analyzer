import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from urllib.parse import quote as urlquote
import flask
from flask import Flask, send_from_directory, send_file, request, session, _request_ctx_stack
import requests

import base64
import xlrd
import datetime
import io
import os
import string
import random
import re

from desktop_layout import layout as desktop_layout
from mobile_layout import layout as mobile_layout
from callbacks import *
from app import app, server, cache, register_before_request

app.layout = desktop_layout
register_before_request(app)

#### File upload intimation
@app.callback(Output('upload_intimation', 'children'),
            [Input('upload-data', 'filename')])
def cb_upload_intimation(filename):
    if filename is not None:
        return dbc.Col(
            [
                html.P(filename + ' successfully uploaded!',
                style = {'text-align':'center'})
            ]
        )

### Choice of sheets if file is xlsx
@app.callback([Output('select-sheet-div', 'style'),
                Output('select-sheet', 'options')],
              [Input('upload-data', 'filename'),
              Input('upload-data', 'contents')])
def cb_sheet_dropdown(filename, contents):
    if filename is not None and 'xls' in filename.lower():
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        file_ = pd.ExcelFile(io.BytesIO(decoded))
        options = [{"label" : sheet, "value" : sheet} for sheet in file_.sheet_names]
        return {'display': 'inline'}, options
    else:
        return {'display': 'none'}, []

#### Decide if the "anlayze" and "downloads" buttons should be active
@app.callback([Output('analyze-button', 'disabled'),
                Output('download-button', 'disabled')],
              [Input('upload-data', 'filename')])
def cb_button_active(filename):
    return filename is None, filename is None

#### Download report

@server.route("/_intermediate/<path:path>")
@cache.memoize(timeout=0)
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory("_intermediate", path, as_attachment=True,
            cache_timeout = 0)

@app.callback(Output('download-button', 'href'),
              [Input('analyze-button', 'n_clicks'),
              Input('memory-output', 'data')])
def cb_download_report(n_clicks, data):
    if n_clicks is not None and data.get('filename') is not None:
        # send_file("_intermediate/report.html", as_attachment=True,
        #     cache_timeout = 0)
        return "/_intermediate/{}".format(urlquote(data.get('filename')))

#### Show report
global clicks 
clicks = 1

@app.callback([Output('output-report', 'children'),
            Output('memory-output', 'data')],
              [Input('analyze-button', 'n_clicks'),
              Input('skiprows', 'value'),
              Input('select-sheet', 'value'),
              Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
              State('memory-output', 'data')])
def cb_create_report(n_clicks, skiprows, sheet_name, contents, filename, data):
    if data is None:
        data = {}
        data['clicks'] = 1

    if contents is not None and filename is not None and n_clicks is not None and data['clicks'] == n_clicks:
        data['clicks'] += 1

        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename.lower():
                # Assume that the user uploaded a CSV file

                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')),
                    skiprows = skiprows)
                valid = True

            elif 'xls' in filename.lower():
                # Assume that the user uploaded an excel file
                if sheet_name is None:
                    sheet_name = 0

                df = pd.read_excel(io.BytesIO(decoded),
                    skiprows = skiprows, sheet_name = sheet_name)
                valid = True

            else:
                valid = False
                print (data, n_clicks)
                return html.Div([
                'There was an error processing this file.'
            ]), data

            if valid:
                report = create_report(df).to_html()
                lettersAndDigits = string.ascii_letters + string.digits
                file_name = 'report_'+"".join(random.sample(lettersAndDigits, 6))+'.html'
                data['filename'] = file_name
                
                with open('_intermediate/'+ file_name, 'w') as file:
                    file.write(report)
                    file.close()
                print (data, n_clicks)
                return html.Iframe(srcDoc = report,
                style={
                    'width': '100%',
                    'height': '100%',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                }), data

        except Exception as e:
            print(e)
            print (data, n_clicks)
            return html.Div([
                'There was an error processing this file.'
            ]), data
        
    else:
        print (data, n_clicks)
        return None, data

##### Calback for collapse #####
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.server.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))