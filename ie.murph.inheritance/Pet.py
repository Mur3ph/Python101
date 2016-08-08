__author__ = 'Paul'

class Pet():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract methos!") #If one of the sub classes does not overrif=de this method it will raise an error




