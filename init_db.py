import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Feedback (feedback_text, sentiment_result) VALUES (?, ?)",
            ('I like the product', 'Positive')
            )

cur.execute("INSERT INTO Feedback (feedback_text, sentiment_result) VALUES (?, ?)",
            ('I hate the product', 'Negative')
            )

connection.commit()
connection.close()
