from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

class InfoForm(FlaskForm):

    breed = StringField("What Breed Are You ?")
    submit = SubmitField("Submit")

@app.route("/",methods = ["GET","POST"])
def index():

    breed = False
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ""

    return render_template("home.html",form = form,breed = breed)

if __name__ == "__main__":
    app.run(debug=True)