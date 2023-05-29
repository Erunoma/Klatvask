import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session

# hvis database til users ik er lavet: sqlite3 database.db ".read db.sql"
# hvis database ik vaskemaskiner ikke er lavet: sqlite3 database.db ".read db2.sql"

def register_user_to_db(username, password, phone_number):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username,password, phone_number, has_a_booking) values (?,?,?,?)', (username, password, phone_number, 0))
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

# opret tom vaskemaskine data
def fill_wash_tabel():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    querry = "INSERT INTO machine_booking(machine_1_2, machine_3_4, username, wash_day, sms_enabled) VALUES(?,?,?,?,?)"
    for i in range(56):
        cur.execute(querry,(0,0,0,0,0))
    con.commit()
    con.close()


# vaskemaskine status
def status_machines():
    fuld_booked = []
    alle_ledige = []
    en_fri = []
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
    return fuld_booked, alle_ledige, en_fri


# updater vaskemaskiner
def update_machines(maskine1, maskine2, id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    var = 'UPDATE machine_booking SET machine_1_2=?, machine_3_4=? WHERE id=?'
    cur.execute(var, (maskine1, maskine2, id))
    con.commit()
    con.close()



app = Flask(__name__)
app.secret_key = "r@nd0mSk_1"


@app.route("/")
def index():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        phone_number = request.form['phone_number']
        if not username or not password or not repeat_password or not phone_number:
            return 'udfyld venligst alle', {"Refresh": "3; url=/register"} 
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

        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/home', methods=['POST', "GET"])
def home():
    if request.form == "book_here":
        return render_template('login.html')

    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return "<h1>forkert kode eller bruger findes ikke</h1>", {"Refresh": "3; url=/login"}
    

@app.route('/reset_password',methods=['POST','GET'])
def reset_password():
    if 'username' in session:
       
            
        
        # fill_wash_tabel() sæt ind hvis du vil fylde vaskedatabasen ud med fyld data.
        return render_template('reset_password.html')
        
    else:
        return 'log ind du!', {"Refresh": "3; url=/login"}


@app.route('/booking')
def booking():
    if 'username' in session:
        
        # fill_wash_tabel() sæt ind hvis du vil fylde vaskedatabasen ud med fyld data.
        return render_template('booking.html')
        
    else:
        return 'log ind du!', {"Refresh": "3; url=/login"}



def get_user_list():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    accounts=cur.execute("SELECT * FROM users").fetchall()
    cur.close()
    return accounts

def delete_account(username):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    print("The user to delete is:",username,".")
    cur.execute("DELETE FROM users WHERE username=?",(username,))
    con.commit()
    cur.close()
    print("The account for",username, "has been deleted.")

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
        return 'log ind du!', {"Refresh": "3; url=/login"}
@app.route('/mod_book')
def modify_bookings():
    if 'username' in session:
        
        # fill_wash_tabel() sæt ind hvis du vil fylde vaskedatabasen ud med fyld data.
        return render_template('modify_bookings.html')
        
    else:
        return 'log ind du!', {"Refresh": "3; url=/login"}

@app.route('/confirm_booking/<id>')
def confirm_booking(id = None):
    if 'username' in session:
        status_machines()
        if status_machines()[1][int(id)]:

            return render_template('confirm_booking.html', id=id, status='alle fri')  
        
        elif status_machines()[2][int(id)]:
            
            return render_template('confirm_booking.html', id=id, status='en ledig')
 


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# flask run -h0.0.0.0 -p80
if __name__ == '__main__':
    
    app.run(debug=True)


