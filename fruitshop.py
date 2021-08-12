
def fruit_menu():
    print("\nPress 1 for Add fruit ")
    print("Press 2 for Delete fruit  ")
    print("Press 3 for Search fruit by name and rate  ")
    print("Press 4 for Change fruit name and rate  ")
    print("Press 5 for Display  ")
    print("Press 6 for Add to cart")
    print("Press 7 to display cart")
    print("Press 8 for exit  ")
    print("\n_____________________________________\n")

def add_fruit():
    fruit_id = int(input("Enter the ID number "))
    if fruit_id not in fruit.keys():
        name = input("Enter Fruit name ")
        rate = input("Enter Fruit rate ")
        imp_frm = input("Imported from : ")
        imp_date = input("Imported date : ")
        price = input("Buy price : ")
        temp = {
            "name":name,
            "rate":rate,
            "imp_frm":imp_frm,
            "imp_date":imp_date,
            "price":price
        }
        fruit[fruit_id] = temp
    else:
        print("ID is already taken")

def delete_fruit():
    fname = input("Enter Fruit name ")
    for idn,frt in (fruit.copy()).items():
        if frt['name'] == fname:
            del fruit[idn]

def search_menu():
    print("Press 1 for search by name ")
    print("Press 2 for search by rate ")
    print("")

def search_name():
    name = input("Enter the fruit name ")
    found = False
    for val in fruit.values():
        if(val['name'] == name):
            found = True
            print(val)
    if(found == False):
        print("not found")

def search_rate():
    rate = input("Enter the rate")
    found = False
    for val in fruit.values():
        if(val['rate'] == rate):
            found = True
            print(val)
    if(found == False):
        print("not found")

def change_menu():
    print("\n Press 1 for change name")
    print("\n Press 2 for change rate")

def change_name():
    newname = input("Enter new name")
    fruit[fruit_id]['name'] = newname

def change_rate():
    newrate = input("Enter new rate")
    fruit[fruit_id]['rate'] = newrate

def display_fruit():
    print(fruit)

def add_to_cart():
    count = 1
    for item in fruit:
        print(count,"." ,item)
        count+=1
    id = int(input("Enter fruit id"))
    cart.append(fruit[id])

def display_cart():
    print(cart)


print("__________Fruit Shop ___________")
fruit = {}
cart = []
while True:
    fruit_menu()
    ch = int(input())
    if(ch == 1):
        add_fruit()
    elif (ch == 2):
        delete_fruit()
    elif(ch == 3):
        search_menu()
        sch = int(input())
        if (sch == 1):
            search_name()
        elif (sch == 2):
            search_rate()
        else:
            print("invalid choice")
    elif(ch == 4):
        fruit_id = int(input("Enter id"))
        if fruit_id not in fruit.keys():
            print("invalid id")
        else:
            change_menu()
            cho = int(input("Enter choice"))
            if(cho == 1):
                change_name()
            elif (cho == 2):
                change_rate()
                
    elif(ch == 5):
        display_fruit()
    elif(ch == 6):
        add_to_cart()
    elif(ch == 7):
        display_cart()
    elif (ch == 8):
        break
    else:
        print("invalid")