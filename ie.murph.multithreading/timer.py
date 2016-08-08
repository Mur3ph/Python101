__author__ = 'Paul'
from threading import Thread
import time

class Timer():

    def timer(self, name, delay, repeat):
        print("Timer: ", name, " started!")
        while repeat > 0:
            time.sleep(delay)
            print(name, ": ", str(time.ctime(time.time())))
            repeat -= 1
        print("Timer: ", name, " completed!")


