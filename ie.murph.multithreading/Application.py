__author__ = 'Paul'
from timer import Timer
from AsyncWrite import AsyncWrite
from lock import MyLock
from threading import Thread
import time

class App():

    def Main1(self):
        print("Multi-Threading..")
        print("Timer..")
        my_timer = Timer()
        thread_1 = Thread(target=my_timer.timer, args=("Timer_1", 1, 5))
        thread_2 = Thread(target=my_timer.timer, args=("Timer_2", 1, 5))
        thread_1.start()
        thread_2.start()
        print("Main Timer completed!")

    def Main2(self):
        print("Asynchronization..")
        try:
            message = input("Enter a string to store:")
        except ValueError:
            print('\n'+"You may only enter strings, thank you!"+'\n'+"Please try again.")
        finally:
            print("Finally always gets executed with or without errors")

        background = AsyncWrite(message, "out.txt")
        background.start()
        print("The program can continue while it writes in another thread")
        print("100 + 400 = ", 100+400)

        background.join()
        print("Waited until thread was complete!")

    def Main(self):
        print("Locks")
        my_timer_lock = MyLock()
        thread_1 = Thread(target=my_timer_lock.timer, args=("Timer_1", 1, 5))
        thread_2 = Thread(target=my_timer_lock.timer, args=("Timer_2", 1, 5))
        thread_1.start()
        thread_2.start()
        print("Main Timer completed!")


x = App()
if __name__ == "__main__":
    x.Main()