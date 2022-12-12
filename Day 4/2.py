# Advent of Code
# Day 4 Assignment 2
#

import sys, os
def main():
    sum = 0
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        contents = f.readlines()
        for i in contents:
            i = i.replace("-",",")
            a, b, c, d = i.split(",")
            A = range(int(a), int(b)+1)
            B = range(int(c), int(d)+1)
            a = overlaps(A, B)
            if a == True or b == True:
                sum += 1
        print(sum)

def overlaps(a:list, b:list):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False

main()