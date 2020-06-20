from flask import Flask
from flask import request
import json
import dataManage

app = Flask(__name__)

data1 = dataManage.dataManage()

@app.route("/api/dados/Brasil")
def get_brasil():
    return json.dumps(data1.region_cases('Brasil').tolist())

@app.route("/api/mortes/Brasil")
def get_deaths_brasil():
    return json.dumps(data1.region_deaths('Brasil').tolist())

@app.route("/api/dados/estado")
def get_state():
    state_name = request.args.get('q')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')
    data1.data = data1.data.loc[start_date:end_date]
    return json.dumps(data1.state_cases(state_name).tolist())

@app.route("/api/mortes/estado")
def get_deaths_state():
    state_name = request.args.get('q')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')
    data1.data = data1.data.loc[start_date:end_date]
    return json.dumps(data1.state_deaths(state_name).tolist())

@app.route("/api/dados/cidade")
def get_city(city_name):
    city_name = request.args.get('q')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')
    data1.data = data1.data.loc[start_date:end_date]
    return json.dumps(data1.city_cases(city_name).tolist())

@app.route("/api/mortes/cidade")
def get_deaths_city(city_name):
    city_name = request.args.get('q')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')
    data1.data = data1.data.loc[start_date:end_date]
    return json.dumps(data1.city_deaths(city_name).tolist())


