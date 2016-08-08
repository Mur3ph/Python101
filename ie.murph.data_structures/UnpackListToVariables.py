__author__ = 'Paul'

class Unpack(object):

    def unpack_to_variables(self):
        #If there is more than 3 data types, it will cause an error. That's when we use Astrix character
        name, age, height = ["Min", 26, 5.6]
        print(name)

    def drop_first_last_calc_average(self, data):
        #Astrix allows us to put all remaining data into middle variable, if there is more than 3 data types
        first, *middle, last = (data)
        average = sum(middle) / len(middle)
        print(average)


x = Unpack()
x.unpack_to_variables()
x.drop_first_last_calc_average([1, 3, 3, 3, 3, 10, 7])