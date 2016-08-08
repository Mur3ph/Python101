__author__ = 'Paul'
#from Pet.py import Pet.class
from Pet import Pet

class Lion(Pet):

    def __init__(self, name, age):
        super().__init__(name, age) # you can run super class methods

    def talk(self):
        return "Rarrrrrrrrrrrrrrrrr.."

