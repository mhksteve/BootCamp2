If_ELse Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions

Equals						-> x == y
Not Equals					-> x != y
Less than					-> x <  y
Less than or equal to		-> x <= y
Greater than				-> x > y
Greater than or equal to	-> x >= y
boolean or 					-> x or y , x | y
Boolean AND					-> x and y , x & y
Boolean Not 				->  not x

#if statement

x = 70
y = 60

if x > y
	print("x is greater than y")


x = 10
if x == 0:
	print("x is zero")			
elif x != 0:
	print("x is equal zero")		#because this condition comes firt than the other correct answers
elif x < 20:
	print("x is 20")
elif x == 10:
	print("x is 10")
else:
	print("x is nothing")


x = 70
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("Default")

x = 456
y = 789

if x == y:
	print("x and y are equal")
elif x != y:
	print("x and y aren't equal")
elif x > y:
	print("x is greater than y")
elif x < y:
	print("x is small than y")
elif x >= y:
	print("x is greater than or equal to y")
elif x <= y:
	print("x is less than or equal to y")
else:
	print("Defualt")


#short hand if
if x < y: print("x is greater than y")

#short hand if...else
x = 50
y = 150
print(x) if x > y else print(y)


#and is logical operator

x = 50
y = 40
z = 100
if x > y and z > y or x > z:
	print("All Conditions are True")
else:
	print("one condition is True")
all conditions are true


x=50
y= 40
z=100
if x > y or z < y:
     print("one of the conditions are true")
elif x > y and z > y:
     print("all conditions are true")
else:
     print("nothing else")

one of the conditions are true

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No, x is not greater than 20")
else:
	print("x is 50")
x is ten
x is greater than 20

---------------------------------------------------------
x = 15

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
		if x > 40 and x < 50 or x == 50:
			print("x is above 40 or equal to 50.")
	else:
		print("No, x is not greater than 20")
else:
	print("x is smaller than 10")
x is ten
no, x is not greater than 20

x = int(input("pleasee enter an interger: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')
	
