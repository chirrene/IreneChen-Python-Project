"""
File: python_random_generator.py
Name: Irene
———————————————————————————————————
This program simulates a certain number of die-roll results and calculates
how many consecutive number (defined as runs) appears.
"""


import random


NUM_ROLLS = 15 #骰15次


def main():
    #初始化
    can_add = True #可不可以加 (因為還沒加過，所以可以加)
    run = 0
    old_roll=random.randrange(1,7) #骰子取隨機數
    for i in range(NUM_ROLLS-1): #骰 14 次，因為前面已經骰一次，前面要先骰，才能比較
        new_roll = random.randrange(1,7)
        if old_roll == new_roll: #判斷可不可以加:不一定 可加可不加需要判斷 can_add
            if can_add: #為何用 can add 系統就能判定是可以加還是不能？can_add 只是一個 true 而已？
                run+=1
                can_add = False #開關 要用 true false 去設定，不然會一直回去跑 if
        else:
            can_add = True #如果 old != new，則開關可以打開，可加
        old_roll = new_roll #永動機 知道上 round 的數字是多少

        print('roll:' + str(new_roll)) #new_roll 才會有 15 次
    print('Number of runs:'+ str(run)) #只需要總共一次 在回圈外


if __name__ == '__main__':
    main()
