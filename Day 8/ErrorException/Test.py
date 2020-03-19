class InputException(Exception):
	'''A user-defined exception class.'''

	def __init__(self, length, atleast, max):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
		self.max = maximum

try:
	text = str(int(input('Enter Your Password: ')))
	
	if len(text) < 8:
		raise InputException(len(text), 8)

	if len(text) > 12:
		raise InputException(len(text), 12)

except ValueError:
	print('This is not interger')

except EOFError:
	print('Why did you do an EOF on me?')

except KeyboardInterrupt:
	print("!! You cancelled the reading from the file")

except InputException as se:
	print(('ShortInputException: The input was ' + '{0} long, expected at least{1}').format(se.length, se.atleast))

except InputException as le:
	print(('LonginputException: The input was ' + ' {0} long, expected at least {1}').format(le.length, le.max))

else:
	print('No exception was raised.')

