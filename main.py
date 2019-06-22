import logging
import webview
from time import sleep
from threading import Thread, Lock
from server.server import run_server
from http.client import HTTPConnection

server_lock = Lock()
logger = logging.getLogger(__name__)


def url_ok(url, port):
    try:
        conn = HTTPConnection(url, port)
        conn.request("GET", "/")
        r = conn.getresponse()
        return r.status == 200
    except:
        logger.exception("Server not started")
        return False


def start_ui():
    w = webview.WebView(width=1080, height=720, title="Flight Finder",
                        url="http://127.0.0.1:5000/", resizable=True, debug=True)
    w.run()


if __name__ == '__main__':
    # logger.info("Starting server")
    # server_thread = Thread(target=run_server)
    # server_thread.daemon = True
    # server_thread.start()
    # logger.info("Checking server")

    while not url_ok("127.0.0.1", 5000):
        sleep(0.1)

    start_ui()

    # logger.info("Server started")
    # gui_thread = Thread(target=start_ui)
    # gui_thread.daemon = True
    # gui_thread.start()
    # logger.info("Starting UI")
