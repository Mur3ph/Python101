__author__ = 'Paul'
#from Pet.py import Pet.class
#from Lion.py import Lion.class
from Pet import Pet
from Lion import Lion
from Wolf import Wolf

class Main():

    def main(self):
        the_pet = Pet("Pet", 1)
        jess = Lion("Jess", 3)

        print("Is Jess a lion ? ", str(isinstance(jess, Lion)))
        print("Is Jess a pet ? ", str(isinstance(jess, Pet)))
        print("Is the pet a lion ? ", str(isinstance(the_pet, Lion)))
        print("Is the pet a pet ? ", str(isinstance(the_pet, Pet)))

        print("Jess name: ", jess.name)

        pets = [Lion("Simba", 11), Wolf("Sheba", 7), Lion("Mufasa", 1), Pet("The-Pet", 69)]

        for pet in pets:
            print("Name: ", pet.name, "Age: ", pet.age, "says", pet.talk())



x = Main()
x.main()



