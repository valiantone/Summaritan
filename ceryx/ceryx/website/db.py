import sqlite3
con = sqlite3.connect("ceryx.db")
cursor = con.cursor()
cursor.execute("Select trend from Sports")
b=[]
a = cursor.fetchall()
b=a[0]
print b
