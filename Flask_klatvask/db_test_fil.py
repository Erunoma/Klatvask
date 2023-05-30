import sqlite3


def status_machines():
    alle_maskiner = []
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
        if row:
            alle_maskiner.append(row)

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
def update_machines(maskine1, maskine2, id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    var = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=? WHERE id=?'
    cur.execute(var, (maskine1, maskine2, id))
    con.commit()
    con.close()
 
"""
#fill_wash_tabel()
update_machines(1,0,1)
status_machines()
print("fuld booked: ", status_machines()[0])
print("alle ledige: ", status_machines()[1])
print("maskine 1 og 2 er ledig: ", status_machines()[2])
print("maskine 3 og 4 er ledig: ", status_machines()[3])

id = 1

for item in status_machines()[0]:
    if item[0] == id:
        print("alle optaget")

for item in status_machines()[1]:
    if item[0] == id: 
        print("alle er ledige")

for item in status_machines()[2]:
    if item[0] == id:
        print("maskine 1 og 2 er ledig")

for item in status_machines()[3]:
    if item[0] == id:
        print("maskine 3 og 4 er ledig")

"""

'''
status_machines()
for i in range(56):
        for item in status_machines()[0]:
            if item[0] == i:
            #if item[0][1] == 1 and item[0][1][1] == '1':
                #print(item[0],item[1], item[2])
                #print(item[:3])
                print(item[0:3])
            else:
                pass
'''

status_machines()
test = []
for i in range(len(status_machines()[0])):
    for item in status_machines()[0]:
        if item[0] == i:
            if item[1:3] == (1,1): 
                        #print(item[0],item[1], item[2])
                        #print(item[:3])
                test.append(i)
   



test = str(test)
test = test.replace('[','').replace(']','').replace(' ', '')
print(len(test))

for i in range(len(test)):
    print(test[i])

print(test)
test_ny = test.split(',')

for i in range(len(test_ny)):
    test_ny[i] = int(test_ny[i])

print(type(test_ny[0]))
print(test_ny)
                    #print(item[0:3])




