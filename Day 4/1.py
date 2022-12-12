# Advent of Code
# Day 4 Assignment 1
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
            a = contains(A, B)
            b = contains(B, A)
            if a == True or b == True:
                sum += 1
        print(sum)

def contains(a:list, b:list):
    result = True
    for i in a:
        if result == True:
            for j in b:
                if i == j:
                    result = True
                    break
                else:
                    result = False
        else:
            return False
    return result
main()