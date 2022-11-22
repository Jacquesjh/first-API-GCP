from flask import Flask

app = Flask(__name__)


@app.route(rule="/")
def index() -> None:
    return "<h1>Rekt Get</h1>"


if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)
