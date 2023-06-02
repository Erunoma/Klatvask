import sqlite3

dum_list = []
dummer_list = []

def booked_machines():
    global dum_list
    global dummer_list
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    #cur.execute('SELECT id, machine_1_2, machine_3_4 FROM machine_booking WHERE machine_1_2=? AND machine_3_4=?', (0, 0))
    cur.execute('SELECT * FROM machine_booking')

    result = cur.fetchall()
    if result[1][1] and result[1][2] == 1:
        for row in result:
            dum_list.append(result)
        return dum_list
         
    else:
        dummer_list.append(result)
        return dummer_list
  
  
def available_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT id FROM machine_booking WHERE machine_1_2=? or machine_3_4=?', (0, 0))
    
    result = cur.fetchone()
    if result:
        dummer_list.append(id)
        return 0
    else:
        return 1

"""
def booking_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT username FROM users WHERE username=?'), (username)
    cur.execute('INSERT True INTO machine_booking (selected_machine)'), (selected_machine,)
"""


def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(machine_1_2, machine_3_4, username, wash_day, sms_enabled) VALUES(?,?,?,?,?)"
    for i in range(56):
        cur.execute(querry,(0,0,0,0,0))
    con.commit()
    con.close()



def booking_machines():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    var = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=? WHERE id=?'
    cur.execute(var, (1, 1, 10))
    con.commit()
    con.close()

def create_admin(username, password, phone_number,admin_status):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username, password, phone_number, has_a_booking, is_admin) values (?,?,?,?,?)', (username, password, phone_number, 0, admin_status))
    con.commit()
    con.close()

create_admin(999,123,88888888,1)
#fill_wash_tabel()
#booking_machines()
#booked_machines()
#print("dum_list: ", dum_list)
#print("dummer_list: ", dummer_list)

# database booking
# database check