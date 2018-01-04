from apscheduler.schedulers.background import  BlockingScheduler #BackgroundScheduler
import os
sched = BlockingScheduler()


def run1():
    print 1
    os.system("cd /usr/local/java/companyDB")
    os.system("java -jar companyDB-1.0-SNAPSHOT.jar")

if __name__ == '__main__':

    sched.add_job(run1, 'interval', id='hy_task', hours=25)
    sched.start()




