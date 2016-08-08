__author__ = 'Paul'

class A(object):

    x = "Ni hao"

    #The "self" variable represents the instance of the object itself (Most other object oriented languages pass this as a hidden parameter in but python does not)
    #The "__init__" function is the constructor for a class
    def __init__(self):
        self.x = "bonjour"

    def method_a(self, foo):
        print(self.x, foo)

    def convert_bitcoin_to_usd(self, bitcoin):
        converted = bitcoin * 527
        print(converted)

    def average_age_Im_allowed_to_date(self, age):
        date_age = age/2 + 7
        if date_age < 18 and age >= 18 and (age - date_age) > 3:
            return "It's against the law creepy, keep walking!"
        return date_age

    #Setting default values to method arguments
    def get_gender(self, sex = "Unknown"):
        if sex is "m":
            sex = "Male"
        elif sex == "f":
            sex = "Female"
        print(sex)

    def sentence(self, name="Spudo", verb="farts", action="gently"):
        print(name, verb, action)


    #Astrix sign allows you to pass ANY number of arguments
    def add_numbers(self, *args):
        total=0
        for a in args:
            total += a
        print(total)

    def calculate_health_rating(self, age, apples_ate_aweek, cigs_smoked):
        answer = (100-age) * (apples_ate_aweek * 3.5) - (cigs_smoked * 2)
        print(answer)


a = A()
print(A.x)
print(a.x)
a.convert_bitcoin_to_usd(1)
a.method_a("adios :)")
print(a.average_age_Im_allowed_to_date(36))
print(a.average_age_Im_allowed_to_date(18))
a.get_gender("m")
a.get_gender()
a.sentence()
a.sentence("SAlly", "is", "so she is")
a.sentence(action="LOUD")

#Using the astrix sign to input unlimited data
a.add_numbers(3)
a.add_numbers(3, 3)
a.add_numbers(3, 3, 45, 23, 23, 32, 54, 100)

#Unpacking Arguments using ASTRIX sign
spudo_data = [35, 8, 0]
a.calculate_health_rating(spudo_data[0], spudo_data[1], spudo_data[2])
a.calculate_health_rating(*spudo_data)
