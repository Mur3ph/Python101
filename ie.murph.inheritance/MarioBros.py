__author__ = 'Paul'
class Mario(object):
    def move(self):
        print("I am moving..")


class Shrooms():

    def get_shrooms(self):
        print("Now I am big!")

# Muliple Inheritance
class BigMario(Mario, Shrooms):
    pass #Does nothing, gives you a pass allowing you to create a class and do nothing


x = BigMario()
x.move()
x.get_shrooms()

3