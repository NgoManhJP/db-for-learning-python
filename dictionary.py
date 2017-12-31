# Dictionary
database = {
	'home' : 'ngoi nha',
	'baby' : 'em be'
}

def show_menu():
	print("--------------------")
	print("CHUONG TRINH TU DIEN")
	print("--------------------")
	print("1. Them tu")
	print("2. Tim tu")
	print("3. Xoa tu")
	print("4. Xem tat ca tu")
	print("An 0 de thoat chuong trinh")
	print("--------------------")

# Add words
def add():
	word = raw_input("tu moi: ")
	mean = raw_input("nghia la: ")
	database[word] = mean
	print("+ Tu moi da duoc them!!!")

# Find
def find():
	word = raw_input("tu gi: ")
	if word in database:
		print("Tim thay: [%s: %s ]" %(word, database[word]))
	else:
		print("Khong tim thay tu: %s" %word)
	
# Delete
def delete():
	word = raw_input("tu gi: ")
	if word in database:
		del database[word]
		print("Tu [%s] da bi xoa" %word)
	else:
		print("Khong tim thay tu: %s" %word)
	
# View all
def view_all():
	for word, mean in database.items():
		print("[%s: %s]" %(word, mean))
	
	
# Hien thi menu
show_menu()	

# Chuong trinh chinh
choice = int(raw_input("Your choice: "))

while choice != 0:
	if choice == 0:
		break
	elif choice == 1:
		#TODO: them tu
		add()
	elif choice == 2:
		#TODO: tim tu
		find()
	elif choice == 3:
		#TODO: xoa tu
		delete()
	elif choice == 4:
		#TODO: xem tat ca
		view_all()
	else:
		print("No choice.")
	choice = int(raw_input("Your choice: ")	)
	
print("See you again!!!")	
	
	
	