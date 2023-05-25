import sqlite3

dum_liste = []
dummmere_liste = []

def booked_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT id FROM machine_booking WHERE machine_1_2=? AND machine_3_4=?', (1, 1))
    
    result = cur.fetchone()
    if result:
        print(result)
        dum_liste.append(id)
        return 1
        
    else:
        print(result)
        return 0
        


def available_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT id FROM machine_booking WHERE machine_1_2=? or machine_3_4=?', (0, 0))
    
    result = cur.fetchone()
    if result:
        dummmere_liste.append(id)
        return 0
    else:
        return 1


def booking_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT username FROM users WHERE username=?'), (username)
    cur.execute('INSERT True INTO machine_booking (selected_machine)'), (selected_machine,)



def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(machine_1_2, machine_3_4, username, wash_day, sms_enabled) VALUES(?,?,?,?,?)"
    for i in range(56):
        cur.execute(querry,(0,0,0,0,0))
    con.commit()
    con.close()



#fill_wash_tabel()
booked_machines()

# database booking
# database check