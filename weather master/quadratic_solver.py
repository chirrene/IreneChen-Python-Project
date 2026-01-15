"""
File: quadratic_solver.py
Name:Irene
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Pre-condition : ax^2+bx+c=0 (a != 0) b^2-4ac
	Post-condition : b^2 − 4ac > 0 (2值), b^2 − 4ac = 0 (1值), b^2 − 4ac < 0 ("No real roots")
	"""
	# 告訴使用者名稱
	print("stanCode Quadratic Solver!")

	# 給 data 下定義 當 input 文字 'Enter X' (以小數形式) > 放到 X 箱 (目的：可以打不同數字做變化)
	a=float(input('Enter a:'))
	b=float(input('Enter b:'))
	c=float(input('Enter c:'))

    # 導入判別式
	discriminate = b*b-4*a*c

	# 三種狀況
	# 當 discriminate > 0, 會有 2 roots
	if discriminate > 0:
		x1=(-b+math.sqrt(discriminate))/(2*a)
		x2=(-b-math.sqrt(discriminate))/(2*a)
		print("Two roots:"+ str(x1) +','+ str(x2))
	# 當 discriminate < 0, 會有 1 root
	# 修正過程 discriminate 已經是0 所以不用再打完整的運算
	elif discriminate==0:
		x=(-b)/(2*a)
		print("One root:"+ str(x))
	# 當 discriminate < 0, 沒有 root
	# else 直接冒號 不用再打 discriminate < 0
	else:
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
