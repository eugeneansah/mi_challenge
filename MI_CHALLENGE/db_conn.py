import sqlite3
from sqlite3 import Error
import json


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_file = "simulation.db"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_by_region_id(conn, region_id):
    """
    Query region_bounding_box table
    :param conn: the Connection object
    :param region_id: the region to get the information
    :return: Row for a region
    """
    cur = conn.cursor()
    cur.execute("SELECT min_latitude,min_longitude,max_latitude,max_longitude FROM region_bounding_box WHERE "
                "region_id=?", (region_id,))
    rows = cur.fetchall()
    if rows:
        return rows[0]
