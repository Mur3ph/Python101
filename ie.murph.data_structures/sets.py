__author__ = 'Paul'

#Sets are a collection of items but can't have duplicates like a list
shopping_list = ["cereal", "milk", "chocolate", "biscuits", "shampoo", "milk"]
print("LIST: ", shopping_list)
shopping_set = {"cereal", "milk", "chocolate", "biscuits", "shampoo", "milk"}
print("SET: ", shopping_set)

def add_grocerie_to_trolley(item):
    if item in shopping_set:
        print("You already have", item, "in trolley")
    else:
        print(item,"added to trolley")
        shopping_set.add(item)


add_grocerie_to_trolley("Milk")
add_grocerie_to_trolley("Peanut butter")

