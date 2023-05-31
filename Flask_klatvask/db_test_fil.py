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

def update_user(book, username):
    con = sqlite3.connect('database.db')
    cur = con.cursor() 
    query = 'UPDATE users SET has_a_booking=? WHERE username=?'
    cur.execute(query, (book, username,))
    con.commit()
    con.close()
    

# tilføj 3 argumenter som skal fodres til vore querry.
def update_machines(maskine1, maskine2, username, wash_day, sms_reminder, id):
    print('print 1')   ####################
    con = sqlite3.connect('database.db')
    cur = con.cursor() 
    print('print 1.5')
    #query = 'SELECT has_a_booking FROM users WHERE id=?'
    query = 'SELECT * FROM users WHERE username=?'
    cur.execute(query, (username,))
    result = cur.fetchall()
    print(result)
    if result[0][4] == 0:
        print('print 2') #################
        query2 = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=?, username=?, wash_day=?, sms_enabled=? WHERE id=?'
        cur.execute(query2, (maskine1, maskine2, username, wash_day, sms_reminder, id))
        con.commit()
        print('print 3') #################
        query3 = 'UPDATE users SET has_a_booking=? WHERE username=?'
        cur.execute(query3, (1, username))
        con.commit()
        con.close()
        print('print 4') ################
        if sms_reminder == 1:
            # sms function
            def send_sms():
                phone_number = result[0][3]
                print('print 5') ##########
                account_sid = 'AC089b2e953b27ca68060de44a7c026d93'
                auth_token = '[AuthToken]'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+13157401145',
                body = f'Hej {username}. Husk din vasketid {wash_day}. ',
                to = f'{phone_number}'
                )
                
                print(message.sid)
                _thread.exit()
            
            scheduler = sched.scheduler(time_module.time, time_module.sleep)
            t = time_module.strptime('2023-05-30 12:28:00', '%Y-%m-%d %H:%M:%S')
            t = time_module.mktime(t)
            scheduler_e = scheduler.enterabs(t, 1, send_sms, ())
            print('print 6') ###############
            _thread.start_new_thread(scheduler.run())

        else:
            # make booking without reminder
            # redirect to my booking
            print('print 7') ################
            con.close()
            print('dont forget your time!!!')
    else:
        print('print 8') ###################
        pass
        # show booking not allowed. 
        
#fill_wash_tabel()
update_user(0, 420)
update_machines(0, 0, 123, 2023-5-30, 1, 16)
status_machines()
#print("fuld booked: ", status_machines()[0])
#print("alle ledige: ", status_machines()[1])
#print("en fri : ", status_machines()[2])


# database booking
# database check
