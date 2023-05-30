### working ###
import sched
import time as time_module
import _thread


def myfunc():
    print('working')
    _thread.exit()

scheduler = sched.scheduler(time_module.time, time_module.sleep)
t = time_module.strptime('2023-05-29 14:53:00', '%Y-%m-%d %H:%M:%S')
t = time_module.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, myfunc, ())

_thread.start_new_thread(scheduler.run())


# source: https://stackoverflow.com/questions/11523918/start-a-function-at-given-time