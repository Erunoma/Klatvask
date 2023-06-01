from datetime import date, datetime
from flask import Flask, redirect, url_for, render_template, request, session

id_slots=112

currentday=date.today()

calenderViewableDays=14



class calender_buttons:
    id=0
    date=""
    timeslot=""
 
def date_data(id):
    button_data=calender_buttons()
    button_data.id=id
    id = int(id)
    print("ID From dates_properties:", id)
    if int(button_data.id) in range(1,9) or int(button_data.id) in range(57,65):
        button_data.date="Monday"
    elif int(button_data.id) in range(9,17) or int(button_data.id) in range(65,73):
        button_data.date="Tuesday"
    elif int(button_data.id) in range(17,25)or int(button_data.id) in range(73,81):
        button_data.date="Wednesday"
    elif int(button_data.id) in range(25,33)or int(button_data.id) in range(81,89):
        button_data.date="Thursday"
    elif int(button_data.id) in range(33,41)or int(button_data.id) in range(89,97):
        button_data.date="Friday"
    elif int(button_data.id) in range(41,49)or int(button_data.id) in range(97,105):
        button_data.date="Saturday"
    elif int(button_data.id) in range(49,57)or int(button_data.id) in range(105,113):
        button_data.date="Sunday"
    else:
        button_data.date="ERROR"

    if id==1 or id==9  or id==17  or id==25  or id==33  or id==41  or id==49  or id==57 or id==65 or id==73 or id==81 or id==89 or id==97 or id==105: 
        button_data.timeslot="7-9"
    elif id==2 or id==10  or id==18  or id==26  or id==34  or id==42  or id==50  or id==58 or id==66 or id==74 or id==82 or id==90 or id==98 or id==106: 
        button_data.timeslot="9-11"
    elif id==3 or id==11  or id==19  or id==27  or id==35  or id==43  or id==51  or id==59 or id==67 or id==75 or id==83 or id==91 or id==99 or id==107: 
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



