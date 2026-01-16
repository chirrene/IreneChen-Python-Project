"""
File: rocket.py
Name:Irene
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    Draws the head, belt, upper, and lower parts of the rocket
    use for loop to draw the rocket
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(3): #0, 1, 2
        for j in range(3-i): #空格空格空格
            print(' ', end="")
        for j in range(i+1): #///
            print('/', end="")
        for j in range(i+1):
            print('\\',end="") #\\ 特殊寫法
        print("")

def belt():
    for i in range(1): #0
        for j in range(1):
            print('+', end="")
        for j in range(6):
            print('=', end="")
        for j in range(1):
            print('+')

def upper():
    for i in range(3): #0, 1, 2
        for j in range(1): #0,1,2>1,1,1
            print('|', end="")
        for j in range(2-i): #0,1,2>2,1,0
            print('.', end="")
        for j in range(i+1): #1,2,3
            print('/'+'\\', end="")
        for j in range(2-i): #0,1,2>2,1,0
            print('.', end="")
        for j in range(1): #0,1,2>1,1,1
            print('|', end="")
        print("")

def lower ():
    for i in range(3): #0, 1, 2
        for j in range(1): #0,1,2>1,1,1
            print('|', end="")
        for j in range(i): #0,1,2
            print('.', end="")
        for j in range(3-i): #3,2,1
            print('\\'+'/', end="")
        for j in range(i): #0,1,2
            print('.', end="")
        for j in range(1): #0,1,2>1,1,1
            print('|', end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
