import sqlite3
import urllib2
import re

def init():
    conn1=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
    c=conn1.cursor()
    c.execute('''drop table if exists trends''')
    c.execute('''create table trends(Trend text, Quotient integer, Class text)''')
    c.close()    

def view():
    conn=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
    c=conn.cursor()
    catL=['Sports','Politics','Media','World','Living','Business','Technology']
    for cat in catL:
        c.execute('''Select * from %s''' % cat)
        rows = c.fetchall()
        for row in rows:
            print row
    conn.commit()
    c.close()

def discard():
    conn=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
    c=conn.cursor()
    c.execute('''drop table if exists trends''')
    conn.commit()
    c.close()

def display(name='trends'):
    conn=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
    c=conn.cursor()
    c.execute('''Select * from %s''' % name)
    rows = c.fetchall()
    if name=='trends':
        print "TQ\t|Genre\t|Trend"
        print "-----------------------------------"
        for row in rows:
            print row[1],"\t|",row[2],"\t|",row[0]
    else:
        print "Source\t|Headline"
        print "----------------------------"
        for row in rows:
            print row[0],"\t|",row[1]
                
    conn.commit()
    c.close()



        
        
                

