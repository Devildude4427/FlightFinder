import sys
import os
import webview
import multiprocessing
from threading import Thread
from flask import Flask
from flightfinder.controller import controller
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def start_app():
    server_thread = Thread(target=start_server)
    server_thread.daemon = True
    gui_thread = multiprocessing.Process(target=start_ui)

    logger.info("Starting the server on localhost:8080...")
    server_thread.start()
    logger.info("Starting the UI for the webview...")
    gui_thread.start()


def start_server():
    if getattr(sys, "frozen", False):
        server = Flask(
            __name__,
            static_folder=os.path.join(sys._MEIPASS, "static"),
            template_folder=os.path.join(sys._MEIPASS, "templates"),
        )
    else:
        server = Flask(__name__, static_folder="static", template_folder="templates")
    server.register_blueprint(controller)
    server.run(host="127.0.0.1", port=8080, debug=True, use_reloader=False)


def start_ui():
    w = webview.WebView(
        width=980,
        height=720,
        resizable=True,
        debug=True,
        url="http://127.0.0.1:8080/",
        title="Flight Finder",
    )
    w.run()
