"""
File: prime_checker.py
Name:Irene
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
	"""
	This program finds the prime among user inputs
	prime == 不能被除了自己和 1 以外的整數整除
	"""
	print ('Welcome to the prime checker !')
	data = int(input('n:')) #右值丟左箱

	while data != EXIT:
		for i in range(2, data): #包含底,不包含data #不能被除了自己和 1 以外的整數整除
			if data % i == 0: #只要能夠和 i 整除，就不是質數
				print(str(data) + ' is not a prime number')
				data = int(input('n:'))
		else: #當 for 迴圈 裡面的程式碼都不成立時
			print(str(data) + ' is a prime number')
			data = int(input('n:'))
	print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
