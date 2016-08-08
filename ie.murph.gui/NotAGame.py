__author__ = 'Paul'
class Enemy(object):

    def __init__(self, name):
        self.lives = 3
        self.enemy = name

    def attack(self):
        print("Ouuuch..")
        self.lives -= 1

    def life(self):
        if self.lives >= 1:
            print(self.enemy, "enemy has", self.lives, "lives left!")
        else:
            print(self.enemy, "enemy has died!")

    def game_in_action(self):
        while self.lives > 0:
            user_input = input("\nPress 'x' for Attack and 'm' for Run-Away\n")
            if user_input == "x":
                self.attack()
            else:
                print(self.enemy, "enemy is still alive")

            self.life()


x = Enemy("Podge")
y = Enemy("Paula")

x.game_in_action()

y.life()

