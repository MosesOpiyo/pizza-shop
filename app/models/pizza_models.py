import sqlite3

class Pizza():
    def pizzaData():
       con = sqlite3.connect("order.db")
       cur = con.cursor()
       cur.execute("CREATE TABLE pizza(id INTERGER PRIMARY KEY,name text,description text,price text,size text,toppings text)")
       con.commit()
       con.close()

