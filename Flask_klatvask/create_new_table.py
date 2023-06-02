import sqlite3
def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(id, machine_1_2, machine_3_4, username, wash_day, timeslot, sms_enabled) VALUES(?,?,?,?,?,?,?)"
    for i in range(1,113):
        cur.execute(querry,(i,0,0,0,0,0,0))
        
    con.commit()
    con.close()

fill_wash_tabel()