class CompanyMember:
	'''Represents any company member.'''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized CompanyMember: {})'.format(self.name))

	def tell(self):
		'''Details about myself.'''
		print('Name:"{}" Age:"{}" '.format(self.name, self.age),end="")

class Owner(CompanyMember):
	'''Represent a member of a company.'''

	def __init__(self, name, age, date):
		CompanyMember.__init__(self, name, age)
		self.date = date
		print('(Initialized Owner: {})'.format(self.name, self.age, self.date))
			
	def tell(self):
		CompanyMember.tell(self)
		print('Day: "{}"'.format(self.date))

class Manager(CompanyMember):
	'''Represent a member of a company.'''
	
	def __init__(self, name, age, salary, date):
		CompanyMember.__init__(self, name, age)
		self.salary = salary
		self.date = date
		print('(Initialized Manger: {}'.format(self.name, self.age, self.salary, self.date))

	def tell(self):
		CompanyMember.tell(self)
		print('Salary: "{:d}" Day: "{}"'.format(self.salary, self.date))

class Staff(CompanyMember):
	'''Represent a member of a companyl.'''

	def __init__(self, name, age, salary, date):
		CompanyMember.__init__(self, name, age)
		self.salary = salary
		self.date = date
		print('(Initialized Staff: {}'.format(self.name))

	def tell(self):
		CompanyMember.tell(self)
		print('Salary: "{:d}" Day: "{}"'.format(self.salary, self.date))

o = Owner('Mr. Steve Zhao', 18, 20)
m = Manager('Mr. Johnson', 25, 500000, 25)
s = Staff('Mr. Zilong', 22, 300000, 30)

print()

members = [o,m,s]
for member in members:
	member.tell()

