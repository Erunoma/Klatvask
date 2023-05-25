import sqlite3

dum_liste = []

def booked_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT id FROM machine_booking WHERE machine_1_2=? AND machine_3_4=?', (0, 0))
    
    result = cur.fetchall()
    if result:
        print(result)
        dum_liste.append(id)
        print(dum_liste)
        return 1
        
    else:
        print(result)
        return 0


def user_look():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (123,))
    
    result = cur.fetchall()
    if result:
        print(result)
        return 1
        
    else:
        print(result)
        return 0
    




#booked_machines()
user_look()