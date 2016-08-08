__author__ = 'Paul'
class Work(object):

    def snap_crackle_pop(self):
        for x in range(1,101):
            if x % 3 == 0 and x % 6 == 0:
                print("Snap")
            elif x % 3 == 0:
                print("Crackle")
            elif x % 6 == 0:
                print("Pop")
            else:
                print(x)