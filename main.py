import logging
import webview
import multiprocessing
from threading import Thread
from server.server import run_server

logger = logging.getLogger(__name__)


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


if __name__ == "__main__":
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    gui_thread = multiprocessing.Process(target=start_ui)

    server_thread.start()
    gui_thread.start()
