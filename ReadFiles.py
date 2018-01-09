file = open("example.txt", 'r')
content = file.read()
print("\n---------")
for i in content:
    print(i)

file.seek(0)
content = file.readlines()
file.close()
print(content)
