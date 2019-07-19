import sqlite3


class Database:
    def __init__(self, query_param, value):
        self.conn = sqlite3.connect("CompositionRoulette.db")
        self.cur = self.conn.cursor()
        self.query_store = query_param
        self.value = value

    def query_func(self):
        try:
            self.cur.execute(self.query_store.format(self.value))
            print(self.cur.fetchall())
            return self.cur.fetchall()

        except sqlite3.OperationalError as e:
            print(e, "OpError")
