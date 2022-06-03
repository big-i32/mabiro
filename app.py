from base64 import encode
from multiprocessing.sharedctypes import Value
from xml.etree.ElementTree import tostring
from flask import Flask,render_template,request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wielanggeitsno/')
def wielanggeitsno():
    return render_template('wielanggeitsno.html')