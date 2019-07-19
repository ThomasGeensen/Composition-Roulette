from Rolling import Generator
import sqlite3

sqlite3.connect("CompositionRoulette.db")

print("How many instruments do you want to generate?", "\n")


def tonumber(n):
    x = n
    print(x)
    print(type(x))

    i = Generator(val=x)
    i.instrument()


n1 = int(input("Enter a number: "))

tonumber(n1)
