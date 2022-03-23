from flask import Flask,render_template,redirect,flash,url_for,session
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

class SimpleForm(FlaskForm):
    breed = StringField("What breed are you ?")
    submit = SubmitField("Click Me.")

@app.route("/",methods = ["GET","POST"])
def message():
    form = SimpleForm()
    if form.validate_on_submit():
        session["breed"] = form.breed.data
        flash(f"You just clicked the button and Breed : {session['breed']}")
        return redirect(url_for("message"))
    return render_template("message.html",form = form)

if __name__ == "__main__":
    app.run(debug=True)