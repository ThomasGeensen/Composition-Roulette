from Rolling import Generator
import sqlite3

sqlite3.connect("CompositionRoulette.db")

print("How many instruments do you want to generate?", "\n")


i = Generator(val=int(input("Enter a number: ")))
i.instrument()
