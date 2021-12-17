import re
import string


def printsomething():
print("Hello from python!")

def PrintMe(v):
print("You sent me: " + v)
return 100;

def SquareValue(v):
return v * v
# print multiplication table of n
def MultiplicationTable(n):
    for i in range(1, 11):
        print(n, 'X', i, '=', (n*i))

# input number n from user
n = int(input('Enter number: '))

# print Multiplication Table
MultiplicationTable(n)