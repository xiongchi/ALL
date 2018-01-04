# coding=utf-8
from da import create_flask_app
from apscheduler.schedulers.background import BackgroundScheduler
import da.main.drawPhoto as dp
import da.main.codeincsv as csv
from da.main import task
from da.utils.configutil import ConfigUtil

app = create_flask_app('config')
sched = BackgroundScheduler()

from config import logger

if __name__ == '__main__':
    logger.info('测试日志')
    host_str = ConfigUtil.getconfig('run', 'host')
    # sched.add_job(task.hy_task, 'interval', max_instances=10, id='hy_task',seconds=80)
    # sched.add_job(task.hy_task, 'cron', max_instances=10,id='hy_task', day_of_week='0-6', hour='9-11,13-15', minute='*/5')
    # sched.add_job(task.chy_task, 'cron', max_instances=3,id='chy_task', day_of_week='0-6', hour='9-11,13-15', minute='*/6')
    # sched.add_job(task.bhy_task, 'cron',max_instances=3, id='bhy_task', day_of_week='0-6', hour='9-11,13-15', minute='*/10')
    # 晚上跑23点一次
    # sched.add_job(dp.get_count_map, 'cron', id='count_task', day_of_week='0-6', hour=23, minute=0, second=0)
    # csv.code_in_csv()
    # sched.add_job(csv.code_in_csv, 'cron', id='code_task', day_of_week='0-6', hour=9, minute=0, second=0)
    # sched.start()
    app.run(host=host_str, port=5000)