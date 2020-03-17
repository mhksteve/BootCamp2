class Person:
	pass #An empty block

p = Person()
print(p)

-------------------------------
Methods

class Person:
	def say_hi(self):
		print('Hello, how are you?')

p = Person()
p.say_hi()
----------------------------------


# __init__ Methods
class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello my name is ', self.name)

p = Person('Swaroop')
p.say_hi()

dog = dog('Name')
dog.color('Black')
dog.owner('U Kaung')

dog.function() 	- bark
				- eat
				- sleep
				- bite

----------------------------------------------------

class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_name(self):
        print('Hello, my name is', self.name, '.')
        
    def say_age(self):
        print('Yes,I am', self.age,'years old.')
        
    def say_name_age(self):
        print('I am',self.name,'and',self.age)
        
    def say_gender(self):
        print('I am a',self.gender,'.')

p = Person('U Ba', '56','man')
p.say_gender()
p.say_age()
p.say_name_age()
ptwo = Person('Daw Mya', '43', 'woman')
p.say_gender()
p.say_name_age()
p.say_age()


------------------------------------------------------

# Class and Object  variables

class Robot:
	"""Represents a robot, with a name."""

	population = 0

	def __init__(self,name):
		"""Initializes the data."""

		self.name = name
		print("(Initializing{})".format(self.name))

		robot.population += 1

	def die(self):
		"""I am dying."""

		print("{} is being destroyed!".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(
				Robot.population))

		def say_hi(self):
			"""Greetting by the robot.
			Yeah, they can do that."""

			print("Greetings, my sister call me{}.".format(self.name))

		@classmethod
		def how_many(cls):
				"""Prints the currenet population."""
				print("we have{:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

driod2 = Robot ("C-3PO")
driod2.say_hi()
Robot.how_many()

driod3 = Robot("Q35")
driod3.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So lets destroy them")
driod1.die()
driod2.die()
driod3.die()

Robot.how_many()


-------------------------------
#Inheritance

class SchoolMember:
	'''Represents any school member.'''

	def __init__(self, name, age):
		self.nmae =nameself.age =age
		print('(Initialized SchoolMember: {})'.format(self.name))

	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age),end="")

	class Teacher(schoolMember):
		'''Represents a student.'''

		def __init__(self, name, age, marks):
			SchoolMember.__init__(self, name, age)
			self.marks = marks
			print('(Initialized Student:{})'.format(self.name))

		def tell(self):
			SchoolMember.tell(self)
			print('Marks: "{:d}"'.format(self.marks))

class Student(SchoolMember):
	'''Represents a Student'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members =[t,s]
for member in members:
	member.tell()