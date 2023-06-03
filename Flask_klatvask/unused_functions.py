"""
@app.route('/select_booking/<id>', methods=["POST","GET"])
def select_booking(id = None):
    
    if 'username' in session:
        username = session['username']
        time_data=request.args.getlist("time_data")
        
        if request.method=='POST':

            if request.form['confirm_button'] == "set1":
                
                username = request.form['username']
                machine_choice = 'machine 1 and 2'
                
                print('knap1')
                
                #return render_template('confirm_booking.html', username=username, id=id, machine_choice=machine_choice)
                return redirect(url_for('confirm_booking', username=username, id=id, machine_choice=machine_choice, time_data=time_data))   
            if request.form['confirm_button'] == "set2":
                
                username = request.form['username']
                machine_choice = 'machine 3 and 4'
                
                print('knap2')                   
                #return render_template('confirm_booking.html', username=username, id=id, machine_choice=machine_choice)
                return redirect(url_for('confirm_booking', username=username, id=id, machine_choice=machine_choice, time_data=time_data))


        status_machines()
        for item in status_machines()[1]:
            if item[0] == int(id):
                
                return render_template('select_booking.html', id=id, status='all taken', username=username)
                
        for item in status_machines()[2]:
            if item[0] == int(id):

                return render_template('select_booking.html', id=id, status='all available', username=username)

        for item in status_machines()[3]:
            if item[0] == int(id):

                return render_template('select_booking.html', id=id, status='machine 1 and machine 2 are available', username=username)

        for item in status_machines()[4]:
            if item[0] == int(id):

                return render_template('select_booking.html', id=id, status='machine 3 and machine 4 are available', username=username)

"""