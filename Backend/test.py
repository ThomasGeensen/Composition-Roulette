import sqlite3

a = 1
b = 'SELECT name FROM instruments ORDER BY RANDOM() LIMIT {}'
c = 'SELECT name FROM instruments ORDER BY RANDOM() LIMIT ?'


# def blabla():
#     conn = sqlite3.connect("CompositionRoulette.db")
#     c = conn.cursor()
#     c.execute(b.format(a))
#     print("one")
#     print(c.fetchall())
#     print("\n")
#     c.execute(c, (1, ))
#     print("two")
#     print(c.fetchall())
#
#
# blabla()


class Foo:
    def __init__(self, c, d):
        self.conn = sqlite3.connect("CompositionRoulette.db")
        self.cur = self.conn.cursor()
        self.e = c
        self.f = d

    def bar(self):
        self.cur.execute(self.e.format(self.f))
        print(self.cur.fetchall())


g = Foo(b, 2)
g.bar()
