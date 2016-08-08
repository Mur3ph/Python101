__author__ = 'Paul'

class CatchingErrors(object):

    #This method is similar to a constructor, "init" is short for initialization or something similar
    def __init__(self, y):
        x = "Hello from init"
        print(x, y)

    def enter_favourite_number(self):
        while True:
            try:
                user_input = int(input("\nWhat's your favourite number?\n"))
                print("What!?\n", user_input, "is really your favourite number")
                break
            except ValueError:
                print("\nYou may only enter numbers, thank you!\nPlease try again.")
            except ZeroDivisionError:
                print("Zero can not be divided by another number")
            except:
                print("If I don't know what error to expect, but it doesn't give a good example of what the problem is..")
            finally:
                print("Finally always gets executed with or without errors")


x = CatchingErrors("Paul")
x.enter_favourite_number()



