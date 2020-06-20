from flask import Flask
import json
import dataManage

app = Flask(__name__)

@app.route("/api/dados/Brasil")
def get_brasil():
    return utils.region_cases(utils.corona, 'Brasil')

