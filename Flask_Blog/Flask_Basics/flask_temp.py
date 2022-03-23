from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/thankyou")
def thank_you():
    first = request.args.get("first")
    last = request.args.get("last")

    upperlet = any(i.upper() for i in first)
    lowerlet = any(i.lower() for i in first)
    digitlet = first[-1].isdigit()
    report = upperlet and lowerlet and digitlet

    return render_template("thankyou.html",first = first, last = last,report = report)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors.html"),404

@app.route("/example")
def example():
    some_variable = "Gokhan"
    dictionary = {"Gokhan" : "Ersoz"}
    return render_template("example.html",some_variable = some_variable,letters = list(some_variable),dictionary = dictionary)


@app.route("/puppy/<name>")
def pup_name(name):
    return render_template("puppy.html",name = name.upper())



if __name__ == "__main__":
    app.run(debug=True)
