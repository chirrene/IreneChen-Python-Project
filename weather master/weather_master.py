"""
File: weather_master.py
Name:Irene
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This constant controls when to stop
Exit = -100 #常數

def main():
	"""
	This program finds the maximum, minimum, average, the number of cold days among user inputs
	"""
	print('stanCode "weather master 4.0" !')
	data=int(input('Next Temperature:(or ' + str(Exit) +' to quit)?'))
	if data == Exit:
		print ('No temperatures were entered.')
	else: # 定義第一筆 + 不等於 Exit 的資料
		maximum = data
		minimum = data
		total = data #計算 average
		count = 1 #計算 average
		cold_days = 0 #計算 the number of cold days

		data = int(input('Next Temperature:(or ' + str(Exit) + ' to quit)?')) #再輸入第二筆數值
		while data != Exit: #當 data 不等於 Exit
			if data > maximum:
				maximum = data #data assign maximum
				data = int(input('Next Temperature:(or ' + str(Exit) + ' to quit)?'))
			if data < minimum:
				minimum = data #data assign minimum
				data = int(input('Next Temperature:(or ' + str(Exit) + ' to quit)?'))
			total += data #total = total + data (第一筆 data+data)
			count += 1 #count = count+1 (1+1)
			if data < 16:
				cold_days += 1 #cold_days = cold_days+1 (0+1)
				data = int(input('Next Temperature:(or ' + str(Exit) + ' to quit)?'))

		print ('Highest temperature =' + str(maximum))
		print ('Lowest temperature =' + str(minimum))
		print ('Average =' + str(total/count))
		print ('Cold days =' + str(cold_days))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
