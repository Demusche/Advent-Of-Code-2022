# Advent of Code
# Day 2 Assignment 1

# 1 for X, 2 for Y, 3 for Z
# win 6, loss 0, draw 3
# A - Rock, B - Paper, C - Scissors | Opponent
# X - Rock, Y - Paper, Z - Scissors | You
# Calculate total score
import sys, os

def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        contents = f.readlines()
        sum = 0
        for i in contents:
            if i == 'A X\n':
                sum = sum + 1 + 3
            elif i == 'A Y\n':
                sum = sum + 2 + 6
            elif i == 'A Z\n':
                sum = sum + 3 + 0
            elif i == 'B X\n':
                sum = sum + 1 + 0
            elif i == 'B Y\n':
                sum = sum + 2 + 3
            elif i == 'B Z\n':
                sum = sum + 3 + 6
            elif i == 'C X\n':
                sum = sum + 1 + 6
            elif i == 'C Y\n':
                sum = sum + 2 + 0
            elif i == 'C Z\n':
                sum = sum + 3 + 3
        print(sum)
        
main()
