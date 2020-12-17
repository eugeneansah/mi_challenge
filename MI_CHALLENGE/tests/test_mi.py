from ..mobility.mi_db import MIData


def test_empty_db(client):
    response = client.get('/')
    assert b'booking_distance_bins' in response.data


def test_status_code(client):
    response = client.get('/')
    status_code = response.status_code
    assert status_code == 200


def test_content(client):
    response = client.get('/')
    content_type = response.content_type
    assert content_type == "application/json"


def test_get_booking_disance():
    data = MIData()
    response = data.get_berlin_booking_distance()
    assert "de_berlin" in response[1]


def test_get_booki(booking_distance):
    data = MIData()
    data.save_booking_distance(booking_distance)
    response = data.get_berlin_booking_distance1("de_cologne")
    assert "de_cologne" in response[1]
