import webview
import multiprocessing
from threading import Thread
from flask import Flask
from flightfinder.controller import controller
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
server = Flask(__name__, static_folder="static", template_folder="templates")
server.register_blueprint(controller)


def start_app():
    server_thread = Thread(target=start_server)
    server_thread.daemon = True
    gui_thread = multiprocessing.Process(target=start_ui)

    logger.info("Starting the server on localhost:5000...")
    server_thread.start()
    logger.info("Starting the UI for the webview...")
    gui_thread.start()


def start_server():
    server.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)


def start_ui():
    w = webview.WebView(
        width=980,
        height=720,
        resizable=True,
        debug=True,
        url="http://127.0.0.1:5000/",
        title="Flight Finder",
    )
    w.run()
