__author__ = 'Paul'
import threading

class Messenger(threading.Thread):

    def run(self):
        #Under score is used when I don't want to use the number, just loop 10 times
        for _ in range(10):
            #One of the built in properties of python Threads class allows use to give the thread a name
            print(threading.currentThread().getName())

x = Messenger(name = "Minnie")
y = Messenger(name = "Fangy")
x.start()
y.start()