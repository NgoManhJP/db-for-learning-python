# file = open("example_w.txt", 'w')
# # file.write("Line 1")
# file.write("Line 2")
# file.close()
numbers = [1, 2, 3]
file = open("numbers.txt", "w")
for i in numbers:
    file.write(str(i) + "\n")
file.close()

file = open("numbers.txt", "a")
file.write("4\n")
file.close()
