"""
Make sure to remove this file access from server, (No one should be able to make GET request on it)
"""

import sqlite3

import pandas as pd

from model import Contact


class Db:
    db: str

    def __init__(self, db: str = "contacts.db"):
        self.db = db

    def insert(self, contact: Contact):
        conn = sqlite3.connect(self.db)
        table = self.db.split(".")[0]
        curr = conn.cursor()

        _ = curr.execute(f"""
            SELECT EXISTS (SELECT 1 FROM {table} WHERE email = '{contact.email}')
        """)

        # Check whether email already taken
        if curr.fetchone()[0] == 1:
            print("Email already taken")
            return

        _ = curr.execute(f"""
            INSERT INTO {table} (first, last, phone, email) VALUES
                ('{contact.first}', '{contact.last}', '{contact.phone}', '{contact.email}')
        """)
        conn.commit()

    def delete(self, id: int):
        conn = sqlite3.connect(self.db)
        table = self.db.split(".")[0]
        curr = conn.cursor()
        _ = curr.execute(f"""
            DELETE FROM {table} WHERE id = {id}
        """)
        conn.commit()

    def get_id_by_email(self, email: str) -> int:
        """
        One email per user, so make sure to validate that table contains
        only unique email
        """
        conn = sqlite3.connect(self.db)
        table = self.db.split(".")[0]
        curr = conn.cursor()
        _ = curr.execute(f"""
            SELECT id FROM {table} WHERE email = '{email}'
        """)
        return curr.fetchone()[0]  # pyright: ignore[reportAny]

    def read(self):
        conn = sqlite3.connect(self.db)
        table = self.db.split(".")[0]
        df = pd.read_sql(f"SELECT * FROM {table}", conn)  # pyright: ignore[reportUnknownMemberType]
        print(df)
