# Advent of Code
# Day 5 Assignment 1

import sys, os
def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        listofStacks = [['T','V','J','W','N','R','M','S'],
                        ['V', 'C', 'P', 'Q', 'J', 'D', 'W', 'B'],
                        ['P','R','D','H','F','J','B'],
                        ['D','N','M','B','P','R','F'],
                        ['B','T','P','R','V','H'],
                        ['T','P','B','C'],
                        ['L','P','R','J','B'],
                        ['W','B','Z','T','L','S','C','N'],
                        ['G','S','L']]
        contents = f.readlines()
        for i in contents:
            a, b, c, d, e ,f = i.split(' ')
            print(int(b), int(d), int(f))
def move(list, amount, From, To):
    pass
  
main()