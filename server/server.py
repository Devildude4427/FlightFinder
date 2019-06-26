import urllib.request
from flask import Flask, render_template

ui_dir = "../user_interface"
server = Flask(__name__, static_folder=ui_dir + "/static", template_folder=ui_dir + "/templates")


def run_server():
    server.run(host="127.0.0.1", port=8080, threaded=True)


if __name__ == "__main__":
    run_server()


@server.route("/")
def landing():
    return render_template("landing.html")


@server.route("/search")
def search():
    request = urllib.request.Request("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/BRS-sky/anywhere/2019-09-01?inboundpartialdate=2019-12-01")
    request.add_header('X-RapidAPI-Host', 'skyscanner-skyscanner-flight-search-v1.p.rapidapi.com')
    request.add_header('X-RapidAPI-Key', '70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95')
    resp = urllib.request.urlopen(request)
    content = resp.read()
    print(content)
    return render_template("search.html")
