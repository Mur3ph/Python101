__author__ = 'Paul'

class Zip(object):

    def zip_two_lists(self):
        first = ["Paul", "Min", "Fang"]
        second = ["Murphy", "Wang", "Wang"]
        names = zip(first, second) # Makes a list of Tuples ([Paul, Murphy], [Min, Wang], [Fang, Wang]) Tuples are immutable objects, basically like a List can't be changed
        for a,b in names:
            print(a, b)


x = Zip()
x.zip_two_lists()

