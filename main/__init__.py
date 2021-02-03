import os
import json

import dash
from flask import Flask

from config import BaseConfig
from utils import import_module

def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapp(server)
    register_blueprints(server)

    return server


def register_dashapp(app):
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
    }

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    apps_dir = basedir + '/dash_apps'

    for folder in os.scandir(apps_dir):
        dash_config_path = folder.path + "/config.json"
        if folder.is_dir() and os.path.isfile(dash_config_path):
            try:
                with open(dash_config_path) as f:
                    dash_config = json.loads(f.read())
                    assets_folder = folder.path + '/resources/'
                    # register each dash app and endpoint.
                    dashapp = dash.Dash(__name__,
                                        server=app,
                                        url_base_pathname=f"/{dash_config['route']}/",
                                        assets_folder=assets_folder,
                                        meta_tags=[meta_viewport])

                    layout = import_module('layout', folder.path+"/layout.py")
                    callbacks = import_module('callbacks', folder.path+"/callbacks.py")

                    with app.app_context():
                        dashapp.title = dash_config['title']
                        dashapp.layout = layout.layout
                        callbacks.register_callbacks(dashapp)
                    # _protect_dashviews(dashapp)
            except Exception as e:
                pass

# For each route, add the property of login_required if we need to perform authentication
# https://stackoverflow.com/questions/52286507/how-to-merge-flask-login-with-a-dash-application/54115197#54115197
# def _protect_dashviews(dashapp):
#     for view_func in dashapp.server.view_functions:
#         if view_func.startswith(dashapp.config.url_base_pathname):
#             dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])


def register_blueprints(server):
    from main.webapp import server_bp

    server.register_blueprint(server_bp)
