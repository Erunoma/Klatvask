import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session
#from twilio.rest import Client
import sched
import time as time_module
import _thread
import datetime
import dates_properties


# hvis database til users ik er lavet: sqlite3 database.db ".read db.sql"
# hvis database ik vaskemaskiner ikke er lavet: sqlite3 database.db ".read db2.sql"

#Registers new users to the database when creating an account
def register_user_to_db(username, password, phone_number):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username, password, phone_number, has_a_booking, is_admin) values (?,?,?,?,?)', (username, password, phone_number, 0, 0))
    con.commit()
    con.close()


# check if user and password match
def check_user(username, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select username,password FROM users WHERE username=? and password=?', (username, password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False

#Checks to see if the user is an admin
def check_admin(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select is_admin FROM users WHERE username=?', (username,))
    result = cur.fetchone()
    print('result fra check admin: ',result)
    if result == (1,):
        return True
    else:
        return False
    

# to check if user exists, so we cant have two users with the same name, and different passwords..    
def check_if_user_exist(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select username FROM users WHERE username=?', (username,))
    
    result = cur.fetchone()
    if result:
        return True
    else:
        return False

#Gets a list of users
def get_user_list():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    accounts=cur.execute("SELECT * FROM users").fetchall()
    cur.close()
    return accounts
#Deletes an account. normally only accessible by admins
def delete_account(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    print("The user to delete is:",username,".")
    cur.execute("DELETE FROM users WHERE username=?",(username,))
    con.commit()
    cur.close()
    print("The account for",username, "has been deleted.")

#Gets the booking information of the users booking
def view_booking(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    bookings=cur.execute("SELECT * FROM machine_booking WHERE username=?", (username,)).fetchall()
    return bookings


# Creates the static database rows for washing machine id's
def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(machine_1_2, machine_3_4, username, wash_day, timeslot, sms_enabled) VALUES(?,?,?,?,?,?)"
    for i in range(224):
        cur.execute(querry,(0,0,0,0,0,0))
    con.commit()
    con.close()


# Check the status of all the washing machines, to see if they are booked or not.
def status_machines():
    alle_maskiner = []
    fuld_booked = []
    alle_ledige = []
    machine_1_2_fri = []
    machine_3_4_fri = []
    con = sqlite3.connect('database.db')
    cur = con.cursor()
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

    return alle_maskiner, fuld_booked, alle_ledige, machine_1_2_fri, machine_3_4_fri

# Users are only able to have one booking at a time. This checks if they already have one.
def update_user_wash_status(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = 'UPDATE users SET has_a_booking=? WHERE username = ?'
    cur.execute(query,(0,username))
    con.commit()
    con.close()


# Clears the row for all data.
def update_machines_simple(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=?, username=?, wash_day=?, timeslot=?, sms_enabled=? WHERE username=?'
    cur.execute(query, (0, 0, 0, 0, 0, 0, username))
    con.commit()
    con.close()

# Updates the database with the booking information.
def update_machines(maskine1, maskine2, username, wash_day, timeslot, sms_reminder, id):
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
        query2 = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=?, username=?, wash_day=?, timeslot=?, sms_enabled=? WHERE id=?'
        cur.execute(query2, (maskine1, maskine2, username, wash_day, timeslot, sms_reminder, id))
        con.commit()
        print('print 3') #################
        query3 = 'UPDATE users SET has_a_booking=? WHERE username=?'
        cur.execute(query3, (1, username))
        con.commit()
        con.close()
        print('print 4') ################
        if sms_reminder == 1:
            pass   # ---------------------------------------- sms sat på pause ---------------------------
            """"
            #time = '2023-05-29 14:53:00'
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
            t = time_module.strptime(wash_day, '%Y-%m-%d %H:%M:%S')
            t = time_module.mktime(t)
            scheduler_e = scheduler.enterabs(t, 1, send_sms, ())
            print('print 6') ###############
            _thread.start_new_thread(scheduler.run())
            """

        else:
            # make booking without reminder
            # redirect to my booking
            print('print 7') ################  
            return 'dont forget your time!!!', {'Refresh': '3; url=/view_booking'}
            
    else:
        print('print 8') ###################
        con.close()
        return 'You already have a booking !!',{"Refresh": "3; url=/view_booking"} 
        # show booking not allowed. 


# Every Week, at the specified time, the database will update its weekly bookings
""""
def weekly_schedule():
    scheduler = sched.scheduler(time_module.time, time_module.sleep)
    t = time_module.strptime("", '%d %H:%M:%S')
    t = time_module.mktime(t)
    scheduler_e = scheduler.enterabs(t, 1, dates_properties.weekchange(), ())
    sleep(1)
    _thread.start_new_thread(scheduler.run())
def start():
    weekly_schedule()
"""


app = Flask(__name__)
app.secret_key = "r@nd0mSk_1"



@app.route("/")
def index():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('login.html')


@app.route('/reset_password',methods=['POST','GET'])
def reset_password():
    if 'username' in session:
       if request.method=='POST':
          username = request.form['username']
          old_password_form=request.form['old_password']
          new_password_form=request.form['new_password']
          new_password_repeat_form=request.form['repeat_password']
          correct_info= check_user(username,old_password_form)
          if correct_info==True:
            if new_password_form == new_password_repeat_form:
                con = sqlite3.connect('database.db')
                cur = con.cursor()
                query = 'UPDATE users SET password=? WHERE username = ?'
                cur.execute(query,(new_password_form,username))
                con.commit()
                con.close()
                return redirect(url_for('home'))
            else:
                return 'The repeated password did not match.',{"Refresh": "3; url=/reset_password"} 
          else:
            return 'The account information provided did not match our database.',{"Refresh": "3; url=/reset_password"}
            
       return render_template('reset_password.html')
    else:
        return 'please log in!', {"Refresh": "3; url=/login"}

        
   

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        phone_number = request.form['phone_number']
        if not username or not password or not repeat_password or not phone_number:
            return 'please fill out everything', {"Refresh": "3; url=/register"}
        if len(username)>3:
            return 'username can only be 3 numbers', {"Refresh": "3; url=/register"}     
        if password != repeat_password:
            return 'password dont match',{"Refresh": "3; url=/register"} 
        if check_if_user_exist(username):
            return '<h1>User already exists</h1>', {"Refresh": "3; url=/login"}    
        else:
            register_user_to_db(username, password, phone_number)
            return redirect(url_for('index'))     
    else:
        return render_template('register.html')



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
       
        if check_user(username, password):
            session['username'] = username
            
            return redirect(url_for('home') )
        else:
            return 'The account information provided did not match our database.',{"Refresh": "3; url=/login"}
    else:
        return redirect(url_for('index'))



@app.route('/home', methods=['POST', "GET"])
def home():
    if request.form == "book_here":
        return render_template('booking2.html')
        
    if 'username' in session:
        print("There is a user here")
        username= session['username']
        is_admin = check_admin(username)
        
        print('sidste skridt: ',is_admin)
        return render_template('home.html', username=session['username'],is_admin=is_admin)
    else:
        return "<h1>wrong password, or the user doesn't exist</h1>", {"Refresh": "3; url=/login"}



@app.route('/booking', methods=["POST","GET"])
def booking():
    if 'username' in session:
      if request.method=="POST":
        button_id=request.form["calender_button"]
       
        if request.form["calender_button"]==str(button_id):
            button_data=dates_properties.date_data(button_id)
            print("ID: ",button_data.id, "Date: ", button_data.date, "Timeslot: ", button_data.timeslot)
            time_data=[button_data.id],[button_data.date],[button_data.timeslot]
            return redirect(url_for('confirm_booking', username=session['username'], id=button_id, time_data=time_data,))
                   

      status_machines()
      temp_list = [] 
      for i in range(len(status_machines()[0])):

        for item in status_machines()[0]:
   
            if item[0] == i:
                if item[1:3] == (1,1):
                        
                        temp_list.append(item[0:1])
                  
      temp_list = str(temp_list)
      temp_list = temp_list.replace('[(','').replace(',)]','').replace('(','').replace(',)','').replace(' ','')
      print(temp_list)
      return render_template('booking2.html', temp_list=temp_list)
       
        
    else:
        return 'please log in!', {"Refresh": "3; url=/login"}


@app.route('/mod_acc', methods=['POST', 'GET'])
def modify_accounts():

    if request.method == 'POST':
        username = request.form.get('accounts')
        print(str(username))
        delete_account(username)
        accounts = get_user_list()
        return render_template("modify_accounts.html", accounts=accounts)
    if 'username' in session:
       accounts = get_user_list()
       return render_template("modify_accounts.html", accounts=accounts)

    else:
        return 'log in!', {"Refresh": "3; url=/login"}
    



@app.route('/view_booking', methods=['POST', 'GET'])
def view_bookings():

    if 'username' in session:
        username=session['username']
        
        if request.method == 'POST':
            if request.form['delete_booking'] == "yes":
                update_machines_simple(username)
                update_user_wash_status(username)
                return redirect(url_for('home'))
                
        bookings = view_booking(username)
        if bookings: #check if user has a booking, if list is empty, user does not have booking
            machine_1_and_2 = bookings[0][1]
            machine_3_and_4 = bookings[0][2]
            washday = bookings[0][4]
            timeslot = bookings[0][5]
            sms_enabled = bookings[0][6]

            if machine_1_and_2 == 1:
                machine_1_and_2 = 'Machine 1 and 2'
            else:
                machine_1_and_2 = ''
            
            if machine_3_and_4 == 1:
                machine_3_and_4 = 'Machine 3 and 4'
            else:
                machine_3_and_4 = ''

            washday = washday.replace("['",'').replace("']",'')
            if bookings[0][0]< 57:
                washday = 'This week',washday
            if bookings[0][0]> 57:
                washday = 'Next week',washday


            timeslot = timeslot.replace("['",'').replace("']",'') 

            return render_template('view_booking.html',username=username,machine_1_and_2=machine_1_and_2, machine_3_and_4=machine_3_and_4, washday=washday, timeslot=timeslot, sms_enabled=sms_enabled)
        else:
            return redirect(url_for('home'))
    else:
        return 'log in please!', {"Refresh": "3; url=/login"}


@app.route('/modify_bookings', methods=['POST', 'GET'])
def modify_bookings():
    if 'username' in session:
        username=session['username']
        
        if request.method == 'POST':
            if request.form['delete_booking'] == "yes":
                update_machines_simple(username)
                update_user_wash_status(username)
                return redirect(url_for('home'))
                

    print(id)
    
  

@app.route('/confirm_booking', methods=['POST','GET'])
def confirm_booking():
    username = request.args.get('username')
    id = request.args.get('id')
    machine_choice = request.args.get('machine_choice')
    time_data=request.args.getlist("time_data")

    if request.method=='POST':
           
        if request.form['final_button'] == "send":
            print('der trykkes på confirm')

            sms_final = request.form.getlist('sms_choice') == "sms_choice_box"
            print('sms_final: ', sms_final)
            if sms_final == False:
                sms_choice = 0
            else:
                sms_choice = 1
                
            if machine_choice == 'machine 1 and 2':
                print('er i sms ja')
                result = update_machines(1,0,username, time_data[1], time_data[2] ,sms_choice, id)
                
            elif machine_choice == 'machine 3 and 4':
                print('er i sms nej')
                result = update_machines(0,1,username,time_data[1], time_data[2], sms_choice, id)
                
            return result
            
    return render_template('confirm_booking.html', username=username, id=id,time_data=time_data)
       

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# flask run -h0.0.0.0 -p80
if __name__ == '__main__':
    
    app.run(debug=True)


