# Sum digits of an integer
print("---Sum digits of an integer---")
number = raw_input("Type a number: ")

result = 0
for i in list(number):
	result += int(i)
print("Result: %d" %result)	