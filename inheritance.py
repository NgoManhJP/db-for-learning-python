# # class Person:
# # 	def __init__(self, name, age):
# # 		self.name, self.age	= name, age

# # 	def getName(self):
# # 		print("Name: %s" %(self.name))

# # 	def getAge(self):
# # 		print("Age: %d" %(self.age))

# # 	def getSex(self):
# # 		print("Sex: %s" %(self.sex))

# # class Male(Person):
# # 	sex = "Male"

# # male = Male("Ngo Manh", 29)
# # male.getName()
# # male.getAge()
# # male.getSex()

# class Foo:
# 	name = "Foo"
# 	def getName(self):
# 		print("Class: Foo")

# class Bar(Foo):
# 	name = "Bar"
# 	def getName(self):
# 		# print("Class: Bar")
# 		print("Atribute name = " + super(Bar, self).name)
# 		super(Bar, self).getName()

# # print(Foo().name)
# # Foo().getName()
# # print(Bar().name)
# # Bar().getName()

# Bar().getName()

class First:
	def getClass(self):
		print("Class First")

class Second(First):
	def getClass(self):
		super()	.getClass()
		print("Class Second")

class Third(Second):
	def getClass(self):
		super().getClass()

third = Third()				
third.getClass()


