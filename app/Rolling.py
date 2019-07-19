from DatabaseConnect import Database
import sqlite3


class Generator:
    def __init__(self, val):
        self.amount = val

    def instrument(self):
        q = '"SELECT name FROM instruments ORDER BY RANDOM() LIMIT ?;"'
        # q = '"SELECT name FROM instruments ORDER BY RANDOM() LIMIT ?;", '
        # q = 'SELECT name FROM instruments ORDER BY RANDOM() LIMIT ?;'
        # q = 'SELECT name FROM instruments ORDER BY RANDOM() LIMIT ?;, '

        try:
            print("Trying database")
            print(type(self.amount))
            print(q)
            d = Database(q, self.amount)
            d.query()
            print("Just tried database")

        except sqlite3.OperationalError as e:
            print(e, "OpError")
        else:
            print("Other Error")






