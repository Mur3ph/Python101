__author__ = 'Paul'
import sets #importing another file I created
import random #importing a file or api from python

#Dictionaries and Sets are created using {}
classmates = {"Bob" : "Bob lives down the bottom", "Min" : "I love Min", "Charle" : "Charlie says..."}

print("Shows all content in dictionary: ", classmates)
print(classmates["Min"])

for key, value in classmates.items():
    print("Key:", key, "Value:", value)

#Sets don't allow duplicates
sets.add_grocerie_to_trolley("Baaaaananaaaaas")
sets.add_grocerie_to_trolley("Baaaaananaaaaas")

x = random.randrange(1, 21)
print(x)

#Min, Max and Sorting. Transfer the dictionary into a Tuple using Zip and then we can work with it better
stocks = {
    "GOOG": 520.54,
    "FB": 76.45,
    "YHOO": 39.28,
    "AMZN": 306.21,
    "AAPL": 99.76
}

print("Minimum", min(zip(stocks.values(), stocks.keys())))
print("Maximum", max(zip(stocks.values(), stocks.keys())))
print("Sorted", sorted(zip(stocks.values(), stocks.keys())))

##################--- Multi Key Sort --- ###################
print("----------------------------------------------------")
from operator import itemgetter
users = [
    {"FirstName": "Joe", "LastName": "Bloggs"},
    {"FirstName": "Mary", "LastName": "Lamb"},
    {"FirstName": "Paul", "LastName": "Murphy"},
    {"FirstName": "Fang", "LastName": "Wang"},
    {"FirstName": "Jenny", "LastName": "Noone"},
    {"FirstName": "Zoe", "LastName": "Bellew"},
    {"FirstName": "Amy", "LastName": "Zhang"},
    {"FirstName": "Paul", "LastName": "Roberts"},
    {"FirstName": "Paul", "LastName": "Jones"},
    {"FirstName": "Paul", "LastName": "Zebra"},
    {"FirstName": "Paul", "LastName": "Ale"},
    {"FirstName": "Min", "LastName": "Wang"}
]

#First loop only sorts by first name and doesn't sort by last name where Ale shoyld be first and Zebra last
for x in sorted(users, key=itemgetter("FirstName")):
    print(x)

print("----------------------------------------------------")
for x in sorted(users, key=itemgetter("FirstName", "LastName")):
    print(x)




