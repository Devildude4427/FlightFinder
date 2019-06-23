import os
from flask import Flask, render_template

ui_dir = "../user_interface"
server = Flask(__name__, static_folder=ui_dir + "/static", template_folder=ui_dir + "/templates")


def run_server():
    server.run(host="127.0.0.1", port=8080, threaded=True)


if __name__ == "__main__":
    run_server()


@server.route("/")
def hello():
    return render_template("landing.html")
