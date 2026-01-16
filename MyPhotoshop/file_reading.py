"""
File: file_reading.py
—————————————————————————————————
This program reads input from a file named “data.txt” and 
processes each line to extract all numerical digits. 
After collecting the digits, the program calculates and 
displays the maximum, minimum, and average values on the console.
"""


FILE = 'data.txt'
FILE1 = 'data_1.txt'


def main():
    #初始化
    minimum = float('inf') #設定最大數字
    maximum = -float('inf') #設定最小數字
    count=0
    total=0
    with open(FILE, "r") as f:
        for line in f:
            if line != "Nan\n": #缺考資料換行
                data = float(line) #將 data 換成小數形式
                if data > maximum:
                    maximum = data
                if data < minimum: #用 if 兩邊都會做，因為第一筆資料會是最大也是最小
                    minimum = data
                total += data #total=total+data
                count += 1 #count = count+1

    if count == 0:
        print ('No data in this file')
    else:
        print('Max : '+ str(maximum))
        print('Min : ' + str(minimum))
        print('Avg : ' + str(total/count))


if __name__ == '__main__':
    main()
