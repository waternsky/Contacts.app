"""
Make sure to remove this file access from server, (No one should be able to make GET request on it)
"""

import sqlite3

import pandas as pd

from model import Contact


class Db:
    def __init__(self, db="contacts.db"):
        self.db = db

    def insert(self, contact: Contact):
        conn = sqlite3.connect(self.db)
        table = self.db.split(".")[0]
        curr = conn.cursor()
        curr.execute(f"""
            INSERT INTO {table} VALUES
                ({contact.id}, '{contact.first}', '{contact.last}', '{contact.phone}', '{contact.email}')
        """)
        conn.commit()

    def read(self):
        conn = sqlite3.connect(self.db)
        table = self.db.split(".")[0]
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        print(df)
