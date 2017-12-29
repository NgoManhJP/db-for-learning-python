# Check a prime number
print("---Prime number Checker---")
number = int(raw_input("Type a number: "))

if number < 2:
	print("Number of entries must be greater than or equal to 2!")
	exit()

is_prime = True

for i in range(2, number/2 + 1):	
	if number % i == 0:
		is_prime = False
		break

if is_prime:
	print("The number %d is a prime number." %number)