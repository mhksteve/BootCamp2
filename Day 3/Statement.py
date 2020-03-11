x = int(input("Examination Result : "))

if x >= 90 and x <= 100:
	print('A')

elif x < 90 and x >= 70:
	print('B')

elif x < 70 and x >= 60:
	print('C')

elif x < 60 and x >= 40:
	print('D')

elif x < 40 and x >= 0:
	print('Fail')
	
else:
	print("Score invalid. Please try again: ")
