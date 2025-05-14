from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector


import sys
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)