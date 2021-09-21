import sqlite3

def viewData():
    con = sqlite3.connect("pizza.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM order")
    row =cur.fetchall()
    con.close()
    return row