from flask import Flask
from flask_cors import CORS

from ..mobility.mi_constant import MiConstants

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from ..simulator.simulator import Simulator
from ..mobility.mi_db import MIData


@app.route('/')
def simulate_mobbility():
    # # check if data has been loaded
    # import os
    mi = MIData()
    # path = os.path.join(os.path.dirname(__file__), '../simulation.db')
    # if (os.path.exists(path)) is False:
    from .load_data import load_data
    load_data()

    # get the longitude and latitude for berlin
    result = mi.get_berlin_region_long_lat()

    # convert tuple with string elements to float
    data = tuple([float(i) for i in result])

    # pass berlin longitude and latitude tuple to simulator
    sim = Simulator(data)

    # Simulate with number of request
    result = sim.simulate(MiConstants.NUMBER_OF_REQUEST)

    # get booking_distance_bins from simulation result
    booking_distance = result["booking_distance_bins"]
    berlin_booking_distance_tuple = (
        "de_berlin", booking_distance['From 0->1km'], booking_distance['From 1->2km'], booking_distance['From 2->3km'],
        booking_distance['From 3->4km'])

    # Save the berlin distance tuple
    mi.save_booking_distance(berlin_booking_distance_tuple)

    return result
