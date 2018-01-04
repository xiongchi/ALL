from time import sleep
import math
from apscheduler.schedulers.background import BlockingScheduler
sched = BlockingScheduler()


def run():
    print 11
    for i in range(0, 100000000):
        print i
        num = i
    print num

# sched.add_job(run, 'interval', max_instances = 2, id = "run", seconds = 1)
sched.add_job(run, 'cron', max_instances=10 ,id='hy_task', second='*/1')
sched.start()