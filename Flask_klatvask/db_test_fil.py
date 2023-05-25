import sqlite3

fuld_booked = []
alle_ledige = []
en_fri = []

def booked_machines():
    global fuld_booked
    global alle_ledige
    global en_fri
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    #cur.execute('SELECT id, machine_1_2, machine_3_4 FROM machine_booking WHERE machine_1_2=? AND machine_3_4=?', (0, 0))
    cur.execute('SELECT * FROM machine_booking')

    result = cur.fetchall()
    for row in result:
        if row[1] == 1 and row[2] == 1:
            fuld_booked.append(row)
         
   
        elif row[1] == 0 and row[2] == 0:
            alle_ledige.append(row)

        elif row[1] == 1 and row[2] == 0:
            en_fri.append(row)

        elif row[1] == 0 and row[2] == 1:
            en_fri.append(row)    

           
  








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
    cur.execute(var, (0, 1, 7))
    con.commit()
    con.close()


#fill_wash_tabel()
booking_machines()
booked_machines()
print("fuld booked: ", fuld_booked)
print("alle ledige: ", alle_ledige)
print("en fri : ", en_fri)

# database booking
# database check