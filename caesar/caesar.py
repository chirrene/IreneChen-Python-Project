"""
File: caesar.py
Name: Irene
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    :param : alpha
    :return: alpha
    當 secret number == n, 26 個字母會分成 26/n 組, 第 26/n 組替代第一組、第一組替代第二組、第二組替代第三組
    """
    number = int(input('Secret number:'))
    ciphered_string = input('What\'s the ciphered string ?:')
    new_ALPHABET = ALPHABET[-number:]+ALPHABET[:-number] #依照 假如 number == 4 > 倒數第 4 個字母到最後 接上 從頭到倒數第 4 個字母

    ans = "" #重串
    for ch in ciphered_string: #迴圈 輸入字串
        if ch not in ALPHABET: #如果不是字母
            return "error"
        else: #是字母
            i=new_ALPHABET.find(ch) # 在 new_ALPHABET 找 輸入的 ch
            ans += ALPHABET[i] #ans=ans+原字母表的位置

    print('The deciphered string is:'+ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
