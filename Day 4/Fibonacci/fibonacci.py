# fibonacci.py

# Fibonacci numbers module

#n = int(input('Please enter a number: '))
#def = function
def fib(n):							#all b values become next value of a

	a, b = 0, 1
	while a < n:
			print(a, end=' ')
			a, b = b, a+b
	print()

# 0 1 1 2 3 5 8 13 21 34 55 89

#Go to Fibonacci Powerpoint

def fib2(n):	#return Fibonacci series up
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]