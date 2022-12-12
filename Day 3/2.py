# Advent of Code
# Day 3 Assignment 2

import sys, os, string

def main():
    letters = list(string.ascii_letters)
    numbers = list(range(1, 53))
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        contents = f.readlines()
        numberofletters_A = [0]*len(letters)
        numberofletters_B = [0]*len(letters)
        numberofletters_C = [0]*len(letters)