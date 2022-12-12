# Advent of Code
# Day 3 Assignment 2

import sys, os, string

def main():
    letters = list(string.ascii_letters)
    numbers = list(range(1, 53))
    sum = 0
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        contents = f.readlines()
        numberofletters_A = [0]*len(letters)
        numberofletters_B = [0]*len(letters)
        numberofletters_C = [0]*len(letters)
        for i in range(0, len(contents), 3):
            index = 0
            for j in letters:
                numberofletters_A[index] = contents[i].count(j)
                numberofletters_B[index] = contents[i+1].count(j)
                numberofletters_C[index] = contents[i+2].count(j)
                if numberofletters_A[index] != 0 and numberofletters_B[index] != 0 and numberofletters_C[index] != 0:
                    print('common letter is: ' + letters[index])
                    sum += numbers[index]
                    break
                index += 1
    print(sum)
main()