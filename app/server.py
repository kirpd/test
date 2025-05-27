import os
from waitress import serve

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


@app.route("/hello")
def hello():
    return "Еще один привет от Flask"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)
    # app.run(host='0.0.0.0', port=port)
