from flask import *
import json
import dataManage

app = Flask(__name__)

covid_br_data = dataManage.dataManage()
covid_br_data.read_data()

@app.route("/api/dados/Brasil")
def get_brasil():
    return json.dumps(covid_br_data.region_cases('Brasil').tolist())

@app.route("/api/mortes/Brasil")
def get_deaths_brasil():
    return json.dumps(covid_br_data.region_deaths('Brasil').tolist())


@app.route("/api/mortes")
def get_deaths_city():
    #Request paremeters
    state_name = request.args.get('state')
    city_name = request.args.get('city')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')

    if state_name:
        if city_name:
            response = Response(json.dumps(covid_br_data.city_deaths(state_name, city_name, start_date, end_date).tolist()))
        else:
            response = Response(json.dumps(covid_br_data.state_deaths(state_name, start_date, end_date).tolist()))
    else:
        response = Response("")

    print(state_name, start_date, end_date)
    return response


@app.route("/api/casos")
def get_state():
    #Request paremeters
    state_name = request.args.get('state')
    city_name = request.args.get('city')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')

    if state_name:
        if city_name:
            response = Response(json.dumps(covid_br_data.city_cases(state_name, city_name, start_date, end_date).tolist()))
        else:
            response = Response(json.dumps(covid_br_data.state_cases(state_name, start_date, end_date).tolist()))
    else:
        response = Response("")

    print(state_name, start_date, end_date)
    return response


#City names here
@app.route("/api/nomes/cidade")
def get_names_city():
    state_name = request.args.get('state')
    try:
        response = Response(json.dumps(covid_br_data.get_name_cities(state_name).tolist()))
    except:
        response = Response("")
        print("owo")

    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/api/nomes/estado")
def get_names_states():
    try:
        response = Response(json.dumps(covid_br_data.get_name_states().tolist()))
    except:
        response = Response('["none"]')
        print("owo")

    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/api/datas")
def get_dates():
    return json.dumps(covid_br_data.get_start_end_date())
