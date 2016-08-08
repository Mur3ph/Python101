__author__ = 'Paul'
import math

#Reverse class using iterators
class Reverse():

    def __init__(self, data):
        self.data = data
        self.legth_of_data = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.legth_of_data == 0:
            raise StopIteration
        self.legth_of_data -= 1
        return self.data[self.legth_of_data]




