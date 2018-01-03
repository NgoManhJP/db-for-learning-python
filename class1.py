class Person:
	# properties
	name = "Ngo Manh"
	age = 29
	male = True

	# methods
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setAge(self, age):
		self.age = age

	def getAge(self):
		return self.age

	def setMale(self, male):
		self.male = male

	def getMale(self):
		return self.male

# instance
person = Person()

# properties
print(person.name)
print(person.age)
print(person.male)

# methods
person.setName("Ngo Tue An")
print(person.getName())

person.setAge(1)
print(person.getAge())

person.setMale(False)
print(person.getMale())









