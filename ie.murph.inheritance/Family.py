__author__ = 'Paul'
class Parent(object):

    def print_last_name(self):
        print("Murphy")

#Class Child inheritanting from Parent class
class Child(Parent):

    def print_first_name(self):
        print("Minnie")

    #Over riding the method from interitant class Parent
    def print_last_name(self):
        print("xXMurphyXx")


child = Child()
child.print_first_name()
child.print_last_name()
