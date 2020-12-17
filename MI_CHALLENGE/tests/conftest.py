import pytest
# import pdb
# pdb.set_trace()
from ..mobility.main import app
from ..mobility.mi_db import MIData


@pytest.fixture
def client():
    # Prepare before your test

    with app.test_client() as client:
        # Give control to your test
        yield client
    # Cleanup after the test run.
    # ... nothing here, for this simple example


@pytest.fixture
def db_cursor():
    yield MIData.create_connection().cursor()


@pytest.fixture
def booking_distance():
    yield "de_cologne", 1, 2, 3, 4
