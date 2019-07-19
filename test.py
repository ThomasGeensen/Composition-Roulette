import sqlite3


def blabla():
    foo = 1
    conn = sqlite3.connect("CompositionRoulette.db")
    c = conn.cursor()
    c.execute('SELECT name FROM instruments ORDER BY RANDOM() LIMIT ?;', (1,))
    print(c.fetchall())

blabla()