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
        return '<Solar %r>' % (self.State)




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rawdata")
def rawdata():
    return render_template("rawdata.html")

@app.route("/testsql")
def testingsql():
    results = db.session.query(Solar.state, Solar.abbr).all() 
    returned_data = []

    for result in results:
        returned_data.append({
            "State_name":result[0],
            "State_abbr":result[1]
        })
    return jsonify(returned_data)










if __name__ == "__main__":
    app.run(debug=True)