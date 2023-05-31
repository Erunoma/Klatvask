from datetime import date, time, datetime
import datetime
import sched
import time

#print('ctime: ', date.ctime(date.today()))
#print('today: ', date.today())
#print(date.today(time.hour(), time.minute()))
#print(datetime.time())
#print(datetime.datetime(date.today()))


#def yolo():
#    print('whoop, whoop !!')


#s = sched.scheduler()
#s.enterabs(datetime(2023, 5, 11, 11, 11, 0, 0).timestamp(), 1, yolo)
#s.run()

time = "11:09"

dateSTR = datetime.datetime.now().strftime("%H:%M" )
if dateSTR == (time):
   #do function
    print(dateSTR)
else:
    # do something useful till this time
    print('else')
    time.sleep(1)
    pass

print(dateSTR)