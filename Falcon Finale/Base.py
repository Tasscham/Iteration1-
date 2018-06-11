import sqlite3
def creation():
    conn = sqlite3.connect('Flacon.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE NBFace
             (nbr text , temps text )''')

def insertion(nb,temps):
    conn = sqlite3.connect('Flacon.db')
    c = conn.cursor()
    c.execute("INSERT INTO NBFace VALUES ('"+str(nb)+"','"+str(temps)+"')")
    conn.commit()
def selection():
    conn = sqlite3.connect('Flacon.db')
    c = conn.cursor()
    cursor = c.execute("select * from NBFace")
    return cursor
   
    
    
