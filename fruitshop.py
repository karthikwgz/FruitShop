print("__________Fruit Shop ___________")
fruit = {}
cart = []
while True:
    print("\nPress 1 for Add fruit ")
    print("Press 2 for Delete fruit  ")
    print("Press 3 for Search fruit by name and rate  ")
    print("Press 4 for Change fruit name and rate  ")
    print("Press 5 for Display  ")
    print("Press 6 for Add to cart")
    print("Press 7 to display cart")
    print("Press 8 for exit  ")
    print("\n_____________________________________\n")
    ch = int(input())
    if(ch == 1):
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

    elif (ch == 2):
        fname = input("Enter Fruit name ")
        for idn,frt in (fruit.copy()).items():
            if frt['name'] == fname:
               del fruit[idn]

    elif(ch == 3):
        print("Press 1 for search by name ")
        print("Press 2 for search by rate ")
        print("")
        sch = int(input())
        if (sch == 1):
            name = input("Enter the fruit name ")
            found = False
            for val in fruit.values():
                if(val['name'] == name):
                    found = True
                    print(val)
            if(found == False):
                print("not found")
        elif (sch == 2):
            rate = input("Enter the rate")
            found = False
            for val in fruit.values():
                if(val['rate'] == rate):
                    found = True
                    print(val)
            if(found == False):
                print("not found")
        else:
            print("invalid choice")
    elif(ch == 4):
        fruit_id = int(input("Enter id"))
        if fruit_id not in fruit.values():
            print("invalid id")
        else:
            print("\n Press 1 for change name")
            print("\n Press 2 for change rate")
            cho == int(input("Enter choice"))
            if(cho == 1):
                newname = input("Enter new name")
                fruit[fruit_id]['name'] = newname
            elif (cho == 2):
                newrate = input("Enter new rate")
                fruit[fruit_id]['rate'] = newrate


    elif(ch == 5):
        print(fruit)
    elif(ch == 6):
        count = 1
        for item in fruit:
            print(count,"." ,item)
            count+=1
        id = int(input("Enter fruit id"))
        cart.append(fruit[id])

    elif(ch == 7):
        print(cart)
    elif (ch == 8):
        break
    else:
        print("invalid")