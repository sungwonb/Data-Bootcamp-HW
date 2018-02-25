from sqlalchemy import create_engine, and_, or_, inspect, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pymysql
import pandas as pd
import numpy as np
import datetime

dt = datetime.datetime
pymysql.install_as_MySQLdb()
Base = automap_base()
engine = create_engine('sqlite:///hawaii.sqlite')
conn = engine.connect()
Base.prepare(engine, reflect=True)
session = Session(engine)

Measurements = Base.classes.measurement
Stations = Base.classes.stations

### Query for list of prcps and tobs in the previous year
#determine first and last dates
last_date = session.query(Measurements.date).group_by(Measurements.date).order_by(Measurements.date.desc()).first().date
first_date = (dt.strptime(last_date, "%Y-%m-%d") - datetime.timedelta(365)).date().isoformat()

# query using determined dates
table = session.query(Measurements.date,func.sum(Measurements.prcp),func.avg(Measurements.tobs)).\
            group_by(Measurements.date).filter(Measurements.date>=first_date).all()
dates, prcps, tobs = zip(*table)

prcps = list(prcps)
dates = list(dates)
tobs = list(tobs)

precipitation = pd.DataFrame({'precipitation':prcps,'tobs':tobs},dates)
precipitation.index.name = 'date'
precipitation = precipitation.reset_index()

dict_prcp = {}
dict_tobs = {}

for row in precipitation.iterrows():
    dict_prcp[row[1][0]] = row[1][1]
    dict_tobs[row[1][0]] = row[1][2]

### Query for List of Stations
df_stations = pd.read_sql("SELECT station,name FROM stations",conn)
dict_stations = {}
for row in df_stations.iterrows():
        dict_stations[row[1][0]] = row[1][1]


### Begin Flask application

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

### Daily Normals function
def daily_normals(date):
    date_query = """
            SELECT * 
            FROM Measurements m
            JOIN Stations s
            ON s.station = m.station
            WHERE m.date LIKE '%-{0}'
            """.format(date)
    
    df_specific_date = pd.read_sql(date_query,conn)
    
    maximum = df_specific_date['tobs'].max()
    minimum = df_specific_date['tobs'].min()
    average = df_specific_date['tobs'].mean()
    
    return [maximum,minimum,average]

### list of dates function
def list_of_dates(start_date,end_date):
    table = db.session.query(Measurements.date).filter(Measurements.date>=start_date,Measurements.date<=end_date).all()
    dates = pd.Series(list(zip(*table)))
    dates = np.unique(np.array(list(dates)[0]))
    
    return dates.tolist()

def list_of_dates_start_only(start_date):
    table = db.session.query(Measurements.date).filter(Measurements.date>=start_date).all()
    dates = pd.Series(list(zip(*table)))
    dates = np.unique(np.array(list(dates)[0]))
    
    return dates.tolist()

@app.route('/')
def welcome():
    return (
        "<font color=blue size=7> Welcome to Sungwon's Hawaii Climate Analysis! </font><br>"
        '<font size=5><b> Available routes: </b><br>'
        '/api/v1.0/precipitation <br>'
        '/api/v1.0/stations <br>'
        '/api/v1.0/tobs <br><br>'
        '<i>Requisite date format: 0000-00-00, year-month-day </i> <br>'
        '/api/v1.0/&lt;start date&gt; <br>'
        '/api/v1.0/&lt;start date&gt;/&lt;end date&gt; </font> <br>'
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    return jsonify(dict_prcp)

@app.route('/api/v1.0/stations')
def stations():
    return jsonify(dict_stations)

@app.route('/api/v1.0/tobs')
def tobs():
    return jsonify(dict_tobs)

@app.route('/api/v1.0/<start>')
def search(start):
        
    Measurements = Base.classes.measurement
    Stations = Base.classes.stations

    dict_start = {}

    list_dates = list_of_dates_start_only(start)
    for day in list_dates:
        day_no_year = day[-5:]
        stats = daily_normals(day_no_year)
        dict_start[day] = {'tmax':stats[0],'tmix':stats[1],'tavg':stats[2]}
    
    return jsonify(dict_start)

@app.route('/api/v1.0/<start>/<end>')
def search_range(start,end):
    dict_startend = {}
    
    Measurements = Base.classes.measurement
    Stations = Base.classes.stations

    list_dates = list_of_dates(start,end)
    for day in list_dates:
        day_no_year = day[-5:]
        stats = daily_normals(day_no_year)
        dict_startend[day] = {'tmax':stats[0],'tmix':stats[1],'tavg':stats[2]}

    return jsonify(dict_startend)

if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    app.run(debug=True)
    raise NotImplementedError()
