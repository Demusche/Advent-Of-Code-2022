# Advent of Code
# Day 1 Assignment 1
import numpy as ny


def main():
    with open('input.txt') as f:
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