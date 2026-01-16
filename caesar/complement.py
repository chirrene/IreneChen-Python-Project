"""
File: complement.py
Name:Irene
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
following the pattern : A -> T, T -> A, G -> C, C -> G
"""


def main():
    """
     :param string:str
     :return: str
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param string: str
    :return : str
    """

    if dna == '':
        print('DNA strand is missing.')

    ans = ""
    for ch in dna:
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'G':
            ans += 'C'
        elif ch == 'C':
            ans += 'G'


    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
