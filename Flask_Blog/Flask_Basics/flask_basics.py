from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Puppy!</h1>"


@app.route("/information")
def info():
    return "<h1>Puppy are cute!</h1>"


@app.route("/puppy/<name>")
def puppy(name):
    pupname = ""
    if name[-1] == "y":
        pupname = name[:-1] + "iful"
    else:
        pupname = name + "y"

    return "<h1>This is a page for {} </h1>".format(pupname.upper())


if __name__ == "__main__":
    app.run(debug=True)
