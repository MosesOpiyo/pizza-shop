import sqlite3

class User():
  def userData():
    con = sqlite3.connect("pizza.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE user(id INTERGER PRIMARY KEY,userID text,Username text,Firstname text,Email_Address text,phone_number text)")
    con.commit()
    con.close()

  def addUserRec(userID,Username,Firstname,Email_Address,phone_number):
    con = sqlite3.connect("order.db")
    cur = con.cursor()
    cur.execute(("INSERT INTO students VALUES(NULS,?,?,?,?,?)",userID,Username,Firstname,Email_Address,phone_number))
    con.commit()
    con.close()



