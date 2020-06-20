from flask import Flask
import json
import dataManage

app = Flask(__name__)

data1 = dataManage.dataManage()

@app.route("/api/dados/Brasil")
def get_brasil():
    return json.dumps(data1.region_cases('Brasil').tolist())

