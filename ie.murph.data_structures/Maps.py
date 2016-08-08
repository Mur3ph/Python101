__author__ = 'Paul'

class Maps():

    def calc(self, cash):
        return  cash * 2

    def using_map(self, method_of_calculation, data):
        return list(map(method_of_calculation, data))

#Taking a list of iterable data and running it through a function
x = Maps()
data = [10, 30, 20]
new_data = list(map(x.calc, data))
print(new_data)

#FINISHED TUTORIAL 50