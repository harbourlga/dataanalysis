import time
from scrapy import cmdline
import os


def timing(hours=0, minutes=0, seconds=0):
	total = hours*60*60 + minutes*60 + seconds
	return total
    

if __name__ == "__main__":
    os.chdir(r'C:\Users\Administrator\Desktop\ppdai\paipaidai_distribution\paipaidai')
    while True:
        try:
            cmdline.execute('scrapy crawl first'.split())
        except Exception as e:
            print e
            time.sleep(minutes=10)
