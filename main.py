from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

#test route
@app.route('/')
#def index():
#    return "<h1>This shit works 1</h1>"

def index():
    first_name = "John"
    last_name = "Doe"
    return render_template("index.html", first_name=first_name, last_name=last_name)

#localhost user
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", username=name)

# CRF Token for forms (important / secret)
app.config['SECRET_KEY'] = "THISisSUPPOSEDtobeAkeyforhidingFormsubmitionsfromhackersCHANGEthisL8ron"

# Create form class
# class NamerForm(FlaskForm):
    # name =
    # submit =

#404 page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

