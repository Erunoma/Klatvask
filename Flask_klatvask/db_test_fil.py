import sqlite3
#from datetime import date
from twilio.rest import Client
import sched
import time as time_module
import _thread


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
            # sms function
            def send_sms():
                account_sid = 'AC089b2e953b27ca68060de44a7c026d93'
                auth_token = '[AuthToken]'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+13157401145',
                body='Hej {room_id}. Husk din vasketid DDHH. ',
                to='+45XXXXXXXX'
                )
                
                print(message.sid)
                _thread.exit()
            
            scheduler = sched.scheduler(time_module.time, time_module.sleep)
            t = time_module.strptime('2023-05-29 14:53:00', '%Y-%m-%d %H:%M:%S')
            t = time_module.mktime(t)
            scheduler_e = scheduler.enterabs(t, 1, send_sms, ())

            _thread.start_new_thread(scheduler.run())

        else:
            # make booking without reminder
            # redirect to my booking
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
