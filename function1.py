def hello(name):
	print("Hello " + name + " !")

hello("Kim")

def sum(list, start =0):
	sum = 0
	i = start
	while i < len(list):
		sum += list[i]
		i += 1
	return sum	
	# for i in list:
		# sum += i
	# return sum

result = sum([1,2,3], 2)	
print("result: %s" %result)