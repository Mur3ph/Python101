__author__ = 'Paul'
import threading
import time

class MyLock():

    def __init__(self):
        self.tLock = threading.Lock()

    def timer(self, name, delay, repeat):
        print("Timer: ", name, " started!")
        self.tLock.acquire()
        print(name, " has acquired a lock!")
        while repeat > 0:
            time.sleep(delay)
            print(name, ": ", str(time.ctime(time.time())))
            repeat -= 1
        print(name, " is releasing the lock")
        self.tLock.release()
        print("Timer: ", name, " completed!")