from datetime import date, datetime
from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

id_slots=112

currentday=date.today()

calenderViewableDays=14

def weekchange():
    con = sqlite3.connect('database.db')
    cur = con.cursor()


    cur.execute("DELETE FROM machine_booking WHERE id<57")
    con.commit()

    bookings=cur.execute("SELECT * FROM machine_booking").fetchall()
    print(bookings[4][0])
    new_bookings=[]
    
    for i in bookings:
        new_bookings.append(i[0])
    print (new_bookings)
    for i in new_bookings:
        if int(i) >=57:
            new_id=int(i)-56
        cur.execute("UPDATE machine_booking SET id=? WHERE id=?", (new_id,int(i)))
        con.commit()
    
    
    querry = "INSERT INTO machine_booking(id,machine_1_2, machine_3_4, username, wash_day, sms_enabled) VALUES(?,?,?,?,?,?)"
    for i in range(57,113):
        cur.execute(querry,(i,0,0,0,0,0))
    con.commit()

    con.close()

    
    
    


class calender_buttons:
    id=0
    date=""
    timeslot=""
 
def date_data(id):
    button_data=calender_buttons()
    button_data.id=id
    id = int(id)
    print("ID From dates_properties:", id)
    if int(button_data.id) in range(1,17):
        button_data.date="Monday"
    elif int(button_data.id) in range(17,33):
        button_data.date="Tuesday"
    elif int(button_data.id) in range(33,49):
        button_data.date="Wednesday"
    elif int(button_data.id) in range(49,65):
        button_data.date="Thursday"
    elif int(button_data.id) in range(65,81):
        button_data.date="Friday"
    elif int(button_data.id) in range(81,97):
        button_data.date="Saturday"
    elif int(button_data.id) in range(97,113):
        button_data.date="Sunday"


    
    elif int(button_data.id) in range(113,129):
        button_data.date="Monday"
    elif int(button_data.id) in range(129,145):
        button_data.date="Tuesday"
    elif int(button_data.id) in range(145,161):
        button_data.date="Wednesday"
    elif int(button_data.id) in range(161,177):
        button_data.date="Thursday"
    elif int(button_data.id) in range(177,193):
        button_data.date="Friday"
    elif int(button_data.id) in range(193,209):
        button_data.date="Saturday"
    elif int(button_data.id) in range(209,225):
        button_data.date="Sunday"
    else:
        button_data.date="ERROR"

    if id==1 or id==2  or id==17  or id==18  or id==33  or id==34  or id==49  or id==50 or id==65 or id==66 or id==81 or id==82 or id==97 or id==98 or id==113 or id==114 or id==129 or id==130 or id==145 or id==146 or id==161 or id==162 or id==177 or id==178 or id==193 or id==194 or id==209 or id==210: 
        button_data.timeslot="7-9"
    elif id==3 or id==4  or id==19  or id==20  or id==35  or id==36  or id==51  or id==52 or id==67 or id==68 or id==83 or id==84 or id==99 or id==100 or id==115 or id==116 or id==131 or id==132 or id==147 or id==148 or id== 163 or id==164 or id==179 or id==180 or id==195 or id==196 or id==211 or id==212: 
        button_data.timeslot="9-11"
    elif id==5 or id==6  or id==21  or id==22  or id==37  or id==38  or id==53  or id==54 or id==69 or id==70 or id==85 or id==86 or id==101 or id==102 or id==117 or id==118 or id==133 or id==134 or id==149 or id==150 or id==165 or id==166 or id==181 or id==182 or id==197 or id==198 or id==213 or id==214: 
        button_data.timeslot="11-13"
    elif id==4 or id==12  or id==20  or id==28  or id==36  or id==44  or id==52  or id==60 or id==68 or id==76 or id==84 or id==92 or id==100 or id==108: 
        button_data.timeslot="13-15"
    elif id==5 or id==13  or id==21  or id==29  or id==37  or id==45  or id==53  or id==61 or id==69 or id==77 or id==85 or id==93 or id==101 or id==109: 
        button_data.timeslot="15-17"
    elif id==6 or id==14  or id==22  or id==30  or id==38  or id==46  or id==54  or id==62 or id==70 or id==78 or id==86 or id==94 or id==102 or id==110: 
        button_data.timeslot="17-19"
    elif id==7 or id==15  or id==23  or id==31  or id==39  or id==47  or id==55  or id==63 or id==71 or id==79 or id==87 or id==95 or id==103 or id==111: 
        button_data.timeslot="19-21"
    elif id==8 or id==16  or id==24  or id==32  or id==40  or id==48  or id==56  or id==64 or id==72 or id==80 or id==88 or id==96 or id==104 or id==112: 
        button_data.timeslot="21-23"
    
    else:
        button_data.timeslot="ERROR"

    
    return button_data



