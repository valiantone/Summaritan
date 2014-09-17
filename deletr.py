import sqlite3

conn=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
c=conn.cursor()
c.execute('''Delete from Living where trend = "Mothers Day 2013"''')
conn.commit()
c.close()
