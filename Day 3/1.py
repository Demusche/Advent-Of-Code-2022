# Advent of Code
# Day 3 Assignment 1
#
# Find common character,
# sum of prioritizes
import sys, os, string

def main():
    letters = list(string.ascii_letters)
    numbers = list(range(1, 53))
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        contents = f.readlines()
        sum = 0
        for i in contents:
            righthalf, lefthalf = split_list(i)
            numberofletters_righthalf = [0]*len(letters)
            numberofletters_lefthalf = [0]*len(letters)
            index = 0
            for j in letters:
                numberofletters_righthalf[index] = righthalf.count(j)
                numberofletters_lefthalf[index] = lefthalf.count(j)
                index += 1
            index = 0
            for j in numberofletters_righthalf:
                if j != 0 and numberofletters_lefthalf[index] != 0:
                    #print("common letter is: " + letters[index])
                    sum += numbers[index]
                    break
                index += 1
        print(sum)        

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
  
main()