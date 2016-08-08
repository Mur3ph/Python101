__author__ = 'Paul'
#from reverse.py import Reverse.class
from reverse import Reverse

class App():

    #Reverse data using Generators, with much less code
    def Reverse(self, data):
        for index in range(len(data)-1, -1, -1): # data -1 length, finish at -1 and step backwards -1
            yield data[index]

    def Main(self):
        #Using class Iterator way 1
        reversed_data_1 = Reverse("Murphy")
        for character in reversed_data_1:
            print(character)

        #Using method Iterator way 2
        reversed_data_2 = self.Reverse("Navan")
        for character in reversed_data_2:
            print(character)

        #Using lambda Iterator way 3
        data = "Other"
        print(list(data[i] for i in range(len(data)-1, -1, -1)))



x = App()
x.Main()
