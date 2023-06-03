from datetime import date, datetime
from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

id_slots=112

currentday=date.today()

calenderViewableDays=14

def weekchange():
    con = sqlite3.connect('database.db')
    cur = con.cursor()


    cur.execute("DELETE FROM machine_booking WHERE id<113")
    con.commit()

    bookings=cur.execute("SELECT * FROM machine_booking").fetchall()
    print(bookings[4][0])
    new_bookings=[]
    
    for i in bookings:
        new_bookings.append(i[0])
    print (new_bookings)
    for i in new_bookings:
        if int(i) >=113:
            new_id=int(i)-112
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
    elif id==7 or id==8  or id==23  or id==24  or id==39  or id==40  or id==55  or id==56 or id==71 or id==72 or id==87 or id==88 or id==103 or id==104  or id==119 or id==120 or id==135 or id==136 or id==151 or id==152 or id==167 or id==168 or id==183 or id==184 or id==199  or id==200 or id==215 or id==216: 
        button_data.timeslot="13-15"
    elif id==9 or id==10  or id==25  or id==26  or id==41  or id==42  or id==57  or id==58 or id==73 or id==74 or id==89 or id==90 or id==105 or id==106 or id==121 or id==122 or id==137 or id==138 or id==153 or id==153 or id==169 or id==170 or id==185 or id==186 or id==201 or id==202 or id==217 or id==218: 
        button_data.timeslot="15-17"
    elif id==11 or id==12  or id==27  or id==28  or id==43  or id==44  or id==59  or id==60 or id==75 or id==76 or id==91 or id==92 or id==107 or id==108 or id==123 or id==124 or id==139 or id==140 or id==155 or id==156 or id==171 or id==172 or id==187 or id==188 or id==203 or id==204 or id==219 or id==220: 
        button_data.timeslot="17-19"
    elif id==13 or id==14  or id==29  or id==30  or id==45  or id==46  or id==61  or id==62 or id==77 or id==78 or id==93 or id==94 or id==109 or id==110 or id==125 or id==126 or id==141 or id==142 or id==157 or id==158 or id==173 or id==174 or id==189 or id==190 or id==205 or id==206 or id==221 or id==222: 
        button_data.timeslot="19-21"
    elif id==15 or id==16  or id==31  or id==32  or id==47  or id==48  or id==63  or id==64 or id==79 or id==80 or id==95 or id==96 or id==111 or id==112 or id==127 or id==130 or id==143 or id==144 or id==159 or id==160 or id==175 or id==176 or id==191 or id==192 or id==207 or id==208 or id==223 or id==224: 
        button_data.timeslot="21-23"
    
    else:
        button_data.timeslot="ERROR"

    
    return button_data



