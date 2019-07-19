import sqlite3


class Database:
    def __init__(self, query, value):
        self.conn = sqlite3.connect("CompositionRoulette.db")
        self.c = self.conn.cursor()
        self.query = query
        self.value = value
        print(self.query)
        print(self.value)

    def query(self):
        q = self.query
        print(q)
        print("Going to query", "\n")

        self.c.execute(q, (self.value, ))

        print("I just did a query", "\n")

        print(self.c.fetchall())

        print("I just printed the data from the query")


