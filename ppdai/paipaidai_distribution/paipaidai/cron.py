import time
import os


def timing(hours=0, minutes=0, seconds=0):
	total = hours*60*60 + minutes*60 + seconds
	return total

def write_pid():
	with open("pid.txt", "w") as f:
		f.write(str(os.getpid()))

if __name__  != '__main__':
	hours = 1
	minutes = 0
	seconds = 0

	write_pid()

	while True:
		os.chdir(r'C:\Users\Administrator\Desktop\ppdai\paipaidai_distribution')
		os.system("scrapy crawl first")
		time.sleep(timing(minutes=1))
		time.sleep(timing(hours, minutes, seconds))

if __name__  == '__main__':
	hours = 1
	minutes = 0
	seconds = 0

	while True:
		os.chdir(r'C:\Users\Administrator\Desktop\ppdai\paipaidai_distribution\paipaidai')
		os.system("python process_sqlite.py")
		time.sleep(timing(minutes=30))
		time.sleep(timing(hours, minutes, seconds))
