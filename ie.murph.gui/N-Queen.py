__author__ = 'Paul'
from itertools import permutations
class Queens(object):

    #Generates a chess game with X's and O's until all Queens are out of eack others path
    def generate_chess_game(self):
        N=8
        sol=0
        cols = range(N)
        for combo in permutations(cols):
            if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
                sol += 1
                print("Solution" + str(sol) + ":" + str(combo) + "\n")
                print("\n".join("o"* i + "X" + "o" * (N-i-1) for i in combo) + "\n\n\n\n")


x = Queens()
x.generate_chess_game()