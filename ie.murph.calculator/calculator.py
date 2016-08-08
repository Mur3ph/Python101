__author__ = 'Paul'
class Calc(object):

     def average_sum_function(self):
        data_set = [1,2,3,4,5]
        return sum(data_set)/len(data_set)

     def mean(self):
        data_set = [1,2,3,4,5]
        total = 0
        for x in data_set:
            total += x
        mean = total/len(data_set)
        print(mean)


     def calculate_volumn(self, height, radius):
        pie = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
        radius_squared = radius ** 2
        surface_area = (2 * pie * radius_squared) + (2 + pie * radius * height)
        volume = pie * radius_squared * height
        print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, 3))
        print("The surface area of the cylinder is {0:.{1}f}cm\u00b2".format(surface_area, 3))


     def binary_and(self, num1, num2):
         return num1 & num2

     def binary_or(self, num1, num2):
         return num1 | num2


calc = Calc()
print(calc.average_sum_function())
calc.mean()
calc.calculate_volumn(32,15)

# --------- BINARY AND OPERATOR I.E. ADDING TWO BINARY NUMBERS. IF BOTH 1 ANSWER EQUAL 1, ELSE ANSWER EQUAL ZERO
num1 = 50 # 110010
num2 = 25 # 011001

answer1 = calc.binary_and(num1, num2) # 010000 = 16
print(answer1)
answer2 = calc.binary_or(num1, num2) # 010000 = 16
print(answer2)

# -------- BINARY RIGHT SHIFT ---------
x = 240    #11110000
y = x >> 2 #00111100
z = x << 2 #

print("RIGHT SHIFT", y)
print("LEFT SHIFT", z)