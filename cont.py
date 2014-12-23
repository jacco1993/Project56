import os
import datetime
import sys
from apscheduler.scheduler import Scheduler
import logging
logging.basicConfig()

today = str(datetime.date.today())
turn = "false"

def run_crawler():
	i = 0
	while i <= 11:
		global turn
		os.system("python crawl.py %s %s" %(i, turn))
		i+=1
		if today != str(datetime.date.today()):
			turn = "true"

if __name__ == '__main__':
	scheduler = Scheduler(standalone=True)
	scheduler.add_cron_job(run_crawler,day_of_week='mon-sun', hour=1)
	print("Running daily!")
	print("Press CTRL+C anytime to quit")
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		pass