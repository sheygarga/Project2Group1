import os 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc, inspect
from flask import (
   Flask,
   render_template,
   jsonify,
   request,
   redirect)
import numpy as np
import pandas as pd
# import plotly.plotly as py
# import plotly.graph_objs as go
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 2. Create an app
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy 
# The database URI("sqlite:///clean_solar_data.db")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///clean_solar_data.db"

db = SQLAlchemy(app)

class Solar(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key = True)
    
    state = db.Column(db.String(50))
    abbr = db.Column(db.String(50))
    electric_Cost = db.Column(db.Float(4))
    install_Date = db.Column(db.Date)
    zipcode = db.Column(db.Float(6))
    size_kw = db.Column(db.Float(5))
    cost_per_Watt = db.Column(db.Float(15))
    c_range = db.Column(db.String(50))
    cancer_Rate = db.Column(db.Float(5))

    def __repr__(self):
        return '<Solar %r>' % (self.state)

class Install(db.Model):
    __tablename__ = 'installs_ecost'

    state = db.Column(db.String(50), primary_key = True)
    abbr = db.Column(db.String(50))
    size_kW = db.Column(db.Float(10))
    size_one = db.Column(db.Float(10))
    size_two = db.Column(db.Float(10))
    size_three = db.Column(db.Float(10))
    cost = db.Column(db.Float(4))

    def __repr__(self):
        return '<Install %r>' % (self.state)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/bar")
def bar():

    results = db.session.query(Install.abbr, Install.size_one,
        Install.size_two, Install.size_three).all()
    labels = []
    dataS = []
    dataM = []
    dataL = []
    for result in results:
        labels.append(result[0])
        dataS.append(result[1])
        dataM.append(result[2])
        dataL.append(result[3])

    return jsonify(labels, dataS, dataM, dataL)

@app.route("/cancer-rate")
def cancer_heatmap():
    return render_template("cancerrate.html")

@app.route("/total-capacity")
def total_heatmap():
    return render_template("totalCapacity.html")
@app.route("/low-capacity")
def low_heatmap():
    return render_template("lowCapacity.html")
@app.route("/med-capacity")
def med_heatmap():
    return render_template("medCapacity.html")
@app.route("/large-capacity")
def high_heatmap():
    return render_template("largeCapacity.html")
@app.route("/elec-cost")
def cost_heatmap():
    return render_template("elecCost.html")

@app.route("/chartData")
def chartData():
    results = db.session.query(
        Install.state, Install.size_kW, Install.size_one, Install.size_two, Install.size_three).all()
    return jsonify(results)

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/barchart")
def bar_chart():
    return render_template("bar.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port, debug=True)
    #app.run(debug=True)
