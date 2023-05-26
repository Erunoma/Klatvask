import sqlite3
from datetime import date


def status_machines():
    fuld_booked = []
    alle_ledige = []
    machine_1_2_fri = []
    machine_3_4_fri = []
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
            machine_3_4_fri.append(row)

        elif row[1] == 0 and row[2] == 1:
            machine_1_2_fri.append(row)    
    return fuld_booked, alle_ledige, machine_1_2_fri, machine_3_4_fri
           

def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(machine_1_2, machine_3_4, username, wash_day, sms_enabled) VALUES(?,?,?,?,?)"
    for i in range(56):
        cur.execute(querry,(0,0,0,0,0))
    con.commit()
    con.close()

# tilføj 3 argumenter som skal fodres til vore querry.
def update_machines(maskine1, maskine2, username, day, sms_reminder, id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = 'SELECT has_a_booking FROM users WHERE id=?'
    cur.execute(query, (id))
    result = cur.fetchone()
    if result == 0:
        query2 = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=?, username=?, wash_day=?, sms_enabled=? WHERE id=?'
        cur.execute(query2, (maskine1, maskine2, username, day, sms_reminder, id))
        con.commit()
        query3 = 'UPDATE users SET has_a_booking=? WHERE id=?'
        cur.execute(query3, (1, id))
        con.commit()
        con.close()
        if sms_reminder == 1:
            # make booking with reminder
            query_reminder = 'UPDATE users SET'
            con.close()
            print('Sending reminder when time')
        else:
            # make booking without reminder
            
            con.close()
            print('dont forget your time!!!')
    else:
        pass
        # show booking not allowed. 

#fill_wash_tabel()
update_machines(1,1,2)
status_machines()
print("fuld booked: ", status_machines()[0])
print("alle ledige: ", status_machines()[1])
print("en fri : ", status_machines()[2])


# database booking
# database check