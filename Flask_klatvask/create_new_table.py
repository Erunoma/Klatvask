import sqlite3
def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(id, machine_1_2, machine_3_4, username, wash_day, timeslot, sms_enabled) VALUES(?,?,?,?,?,?,?)"
    for i in range(1,245):
        cur.execute(querry,(i,0,0,0,0,0,0))
        
    con.commit()
    con.close()

fill_wash_tabel()

def create_admin(username, password, phone_number,admin_status):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username, password, phone_number, has_a_booking, is_admin) values (?,?,?,?,?)', (username, password, phone_number, 0, admin_status))
    con.commit()
    con.close()

create_admin(999,123,88888888,1)