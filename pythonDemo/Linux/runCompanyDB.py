from apscheduler.schedulers.background import  BlockingScheduler #BackgroundScheduler
import os
import subprocess
sched = BlockingScheduler()


#  && same time run multiple shell command
def run1():
    try:
        subprocess.call("cd /usr/local/java/companyDB/ && nohup java -jar companyDB-1.0-SNAPSHOT.jar & ", shell=True)
    except KeyboardInterrupt, e:
        print "break out"

    # os.system("java -jar companyDB-1.0-SNAPSHOT.jar")

if __name__ == '__main__':
    run1()
    sched.add_job(run1, 'interval', id='hy_task', hours=25)
    sched.start()




