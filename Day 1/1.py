# Advent of Code
# Day 1 Assignment 1
import sys, os
def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        contents = f.readlines()
        mySet = set()
        sum = 0
        for i in contents:
            if i == "\n":
                mySet.add(sum) 
                sum = 0
            else:
                sum = int(i) + sum
        print(max(mySet))
main()