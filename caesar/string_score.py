"""
File: string_score.py
Name: Irene
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
      :param string: including alpha and int
      :return: int, total score
      following the pattern : digit->1 ; upper->2; lower->3
    """
    score('1aB4rC')
    # 12
    score('aaaaA3')
    # 15

    print(score('1aB4rC'))
    print(score('aaaaA3'))


def score(string): #化名 string
    """
      :param string: including alpha and int
      :return: int, total score
      following the pattern : digit->1 ; upper->2; lower->3
    """
    total = 0 #初始化
    for ch in string :
        if ch.isdigit():
            total+=1
        elif ch.isupper():
            total+=2
        elif ch.islower():
            total+=3
    return total








if __name__ == '__main__':
    main()