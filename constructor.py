class Person:
	def __init__(self, name, age, male):
		print("Class Person duoc khoi tao!")
		#print("Name: %s - Age: %d - Male: %d" %(name, age, male))
		self.name, self.age, self.male = name, age, male

	def getName(self):
		print("Name: %s" %(self.name))

	def getAge(self):
		print("Age: %d" %(self.age))

	def getMale(self):
		print("Male: %d" %(self.male))

	def __del__(self):
		print("Class Person duoc huy")

person = Person("Ngo Manh", 29, True)
person.getName()
person.getAge()
person.getMale()
