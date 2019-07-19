from DatabaseConnect import Database
import sqlite3


class Generator:
    def __init__(self, val):
        self.amount = val

    def instrument(self):
        b = 'SELECT name FROM instruments ORDER BY RANDOM() LIMIT {}'
        try:
            dbq = Database(b, self.amount)
            dbq.query_func()

            return None

        except sqlite3.OperationalError as e:
            print(e, "OpError")
        else:
            print("Other Error")






