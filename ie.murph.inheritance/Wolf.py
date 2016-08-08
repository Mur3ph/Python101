__author__ = 'Paul'
from Pet import Pet

class Wolf(Pet):

    def __init__(self, name, age):
        super().__init__(name, age) # You can run the super class methods

    def talk(self):
        return "woofff-a-rooooooooooo"


