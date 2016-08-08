__author__ = 'Paul'
from threading import Thread
import time

class AsyncWrite(Thread):

    def __init__(self, text, out):
        Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("Finished background file write to ", self.out)



