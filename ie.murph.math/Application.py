__author__ = 'Paul'
from vector2d import Vector2D

class App():

    def Main(self):
        vec_1 = Vector2D(5, 6)
        vec_2 = Vector2D(2, 3)
        print(vec_1)
        print(vec_2)

        #Store a function in  variable
        temp_method = vec_1.getAngle #If we don't use the () after on the method, we just stoer the method reference

        vec_1 = vec_1 + vec_2
        print(vec_1)

        vec_1 += vec_2
        print(vec_1)

        vec_1 *= Vector2D(2, 2)
        print(vec_1)

        print(vec_1.normalized())
        print(vec_1.getAngle())

        print(vec_1.getLengthOfVector())

        #Calculations will be different as already altered above, before this was called
        print(temp_method())




x = App()

if __name__ == "__main__":
    x.Main()

