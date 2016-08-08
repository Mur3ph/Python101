__author__ = 'Paul'
from operator import attrgetter

class User():

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    #Object representation
    def __repr__(self):
        return self.name + ":" + str(self.user_id)



#x = User()

users = [
    User("Joe", 13),
    User("Paul", 99),
    User("Mary", 44),
    User("Joe", 65),
    User("Fang", 13),
    User("Jenny", 74),
    User("Zoe", 34),
    User("Joe", 43),
    User("Min", 20),
    User("Joe", 13)
]

for user in users:
    print(user)

print("----------------------------------------------------")
for user in sorted(users, key=attrgetter("name")):
    print(user)

print("----------------------------------------------------")
for user in sorted(users, key=attrgetter("user_id")):
    print(user)

#FINISHED TUTORIAL 56