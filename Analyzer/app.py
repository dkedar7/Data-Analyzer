import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask
from flask import request

import re
from desktop_layout import layout as desktop_layout
from mobile_layout import layout as mobile_layout

external_stylesheets = [dbc.themes.BOOTSTRAP,
"https://use.fontawesome.com/releases/v5.9.0/css/all.css"]

server = flask.Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                server=server)
cache = Cache(app.server)
app.title = "Data Analyzer"

def register_before_request(app):

    @app.server.before_request
    def before_request_func():      # pylint: disable=W0612
        """Checks if user agent is from mobile to determine which layout
        to serve before user makes any requests.
        """
        agent = request.headers.get("User_Agent")
        mobile_string = ("(?i)android|fennec|iemobile|iphone|opera"
                        " (?:mini|mobi)|mobile")
        re_mobile = re.compile(mobile_string)
        is_mobile = len(re_mobile.findall(agent)) > 0

        if is_mobile:
            app.layout = mobile_layout
        else:  # Desktop request
            app.layout = desktop_layout