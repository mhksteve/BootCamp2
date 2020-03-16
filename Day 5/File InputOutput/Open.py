# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

# open & Read File

# f = open('test.txt', 'r')	#R - read
# print(f.name)
# f.close()

# with open('test.txt', 'a') as f:
# 	f.write('This is line number '+"\n")
# 	print(f, end=' ')

# with open('test.txt', 'r') as f:

	# f_text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

with open('test.txt', 'r') as f:

	# f_text = f.readline()
	# print(f_text,end='')

	# for f_text in f:
	# 	print(f_text,end='')

	f_text = f.read(100)
	print(f_text,end=' ')

# 	f_text = f.read(100)

# 	while 100 > 0:
# 		print(f_text,end=' ')