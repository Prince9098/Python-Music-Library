import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST','127.0.0.1'),
            'port': int(os.getenv('DB_PORT',3306)),
            'user': os.getenv('DB_USER','ml_user'),
            'password': os.getenv('DB_PASS','ml_pass'),
            'database': os.getenv('DB_NAME','music_library'),
            'autocommit': True
        }
        self._conn = None
        self.connect()

    def connect(self):
        if self._conn:
            try:
                self._conn.ping(reconnect=True, attempts=1, delay=0)
                return
            except:
                self._conn.close()
        self._conn = mysql.connector.connect(**self.config)

    def ping(self):
        if not self._conn or not self._conn.is_connected():
            self.connect()
        return True

    def query_all(self, query, params=()):
        self.connect()
        cur = self._conn.cursor(dictionary=True)
        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
        return rows

    def execute(self, query, params=()):
        self.connect()
        cur = self._conn.cursor()
        cur.execute(query, params)
        cur.close()

    def insert(self, query, params=()):
        self.connect()
        cur = self._conn.cursor()
        cur.execute(query, params)
        lastid = cur.lastrowid
        cur.close()
        return lastid
