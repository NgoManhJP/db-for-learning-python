#Loop in Dictionary

data = {
	"eggs" : 10,
	"fishes" : 2
}

# Print keys 1
for k in data:
	print (k)
	
# Print keys 2
for k in data.keys():
	print(k)
	
# Print values
for k in data.values():
	print(k)

# Print keys and values	1
for k in data:
	print("Key: %s - Value: %s" %(k, data[k]))

# Print keys and values	2
for k, v in data.items():
	print("Key: %s - Value: %s" %(k, v))