from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from load_data import load_data
from db_conn import *
from simulator.simulator import Simulator
 
@app.route('/')
def hello_world():
    number_of_requests = 10
    load_data()
    conn = create_connection()
    result = select_by_region_id(conn, "de_berlin")
    # print(result)
    result = (13.340148, 52.527919, 13.506317, 52.562995)
    sim = Simulator(result)
    result = sim.simulate(number_of_requests)
    # print(sim)
    # print(result)
    # json_str = json.dumps(dict(result))
    # json.dumps(dict(cursor.fetchall()))
    # print(json.dumps(result))
    # print(result.replace("/\\/g",""))

    # print(json_str)
    return result
