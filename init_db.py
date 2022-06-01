import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (name, title, content) VALUES (?, ?, ?)",
            ('Jan Kowalski', 'Dzialanie strony', 'Ta strona nie chce mi dzialac')
            )

cur.execute("INSERT INTO posts (name, title, content) VALUES (?, ?, ?)",
            ('Nadia Nowak', 'Szukam kolegow', 'Poszukuje kolegow w swoich wieku')
            )

connection.commit()
connection.close()