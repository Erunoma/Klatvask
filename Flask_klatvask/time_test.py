from datetime import date, time, datetime
import datetime
import sched


#print('ctime: ', date.ctime(date.today()))
#print('today: ', date.today())
#print(date.today(time.hour(), time.minute()))
#print(datetime.time())
#print(datetime.datetime(date.today()))


def yolo():
    print('whoop, whoop !!')


s = sched.scheduler()
s.enterabs(datetime(2023, 5, 11, 11, 11, 0, 0).timestamp(), 1, yolo)
s.run()