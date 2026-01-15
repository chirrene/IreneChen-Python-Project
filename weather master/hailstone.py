"""
File: hailstone.py
Name:Irene
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Pre-condition : n (if n == even > n/2, if n==odd > n*3+1)
    Post-condition : n=1
    """
    print('This program computes Hailstone sequence.')
    print(' ') # 空行

    n=int(input('Enter a number:')) #variable
    while n!=1: #看結尾
        if n%2==0:
            print(str(n) + ' is even, so I make half: ' + str(n // 2))
            n=n//2 #reassign #沒有小數點所以選 floor division # print 完，再改變 n
        else:
            print(str(n) + ' is odd, so I make 3n+1:' + str(3 * n + 1))
            n=n*3+1 #reassign


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
