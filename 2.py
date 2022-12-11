# Advent of Code
# Day 1 Assignment 1
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
        result = max(mySet) 
        mySet.remove(max(mySet)) 
        result = max(mySet) + result
        mySet.remove(max(mySet))
        result = max(mySet) + result
        print(result)
main()