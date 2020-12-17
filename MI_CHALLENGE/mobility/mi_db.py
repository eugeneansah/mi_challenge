import sqlite3
from sqlite3 import Error
import os

class MIData:

    @staticmethod
    def create_connection():
        db_file = "../simulation.db"
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

# get longitude and latitude for berlin only
    def get_berlin_region_long_lat(self):
        conn = self.create_connection()
        # rows = None
        # import pdb
        # pdb.set_trace()
        try:
            region_id = "de_berlin"
            cur = conn.cursor()
            cur.execute(
                "SELECT min_longitude, min_latitude, max_longitude, max_latitude FROM region_bounding_box WHERE "
                "region_id=?",
                (region_id,))
            rows = cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()

        if rows:
            return rows[0]

# get booking distance for berlin only
    def get_berlin_booking_distance(self):
        conn = self.create_connection()
        rows = None
        try:
            region_id = "de_berlin"
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM booking_distance WHERE "
                "region_id=?",
                (region_id,))
            rows = cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()

        if rows is not None:
            return rows[0]

# get booking distance for any region specified
    def get_berlin_booking_distance1(self, region_id):
        conn = self.create_connection()
        rows = None
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM booking_distance WHERE "
                "region_id=?",
                (region_id,))
            rows = cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()

        if rows is not None:
            return rows[0]

    # def save_booking_distance(self, from_0_1, from_1_2, from_2_3, from_3_4):
    #     conn = self.create_connection()
    #     region = "de_berlin"
    #     try:
    #         query = "INSERT INTO booking_distance(id, region_id, from_0_1, from_1_2, from_2_3, from_3_4) VALUES (" \
    #                 "NULL, ?, ?, ?, ?, ?) "
    #
    #         cur = conn.cursor()
    #         cur.execute(query, (region, from_0_1, from_1_2, from_2_3, from_3_4))
    #         conn.commit()
    #     except Exception as ex:
    #         print(ex)
    #     finally:
    #         conn.close()

# Save booking distance
    def save_booking_distance(self, booking_diantance):
        conn = self.create_connection()
        try:
            query = "INSERT INTO booking_distance(id, region_id, from_0_1, from_1_2, from_2_3, from_3_4) VALUES (" \
                    "NULL, ?, ?, ?, ?, ?) "

            cur = conn.cursor()
            cur.execute(query, booking_diantance)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()


    # def load_data(self):
    #   try:
    #     conn = sqlite3.connect('simulation.db')
    #     file_path = os.path.join(os.path.dirname(__file__), 'seed_data.sql')
    #     sql_statements = open(file_path).read()
    #     with conn:
    #       cursor = conn.cursor()
    #       cursor.executescript(sql_statements)
    #       conn.commit()
    #     conn.close()
    #     print("All data seeded")
    #   except Error as err:
    #     print(str(err))