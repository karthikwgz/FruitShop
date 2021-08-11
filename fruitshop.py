print("__________Fruit Shop ___________")
fruit = []
while True:
    print("Press 1 for Add fruit ")
    print("Press 2 for Delete fruit  ")
    print("Press 3 for Search fruit by name and rate  ")
    print("Press 4 for Change fruit name and rate  ")
    print("Press 5 for Display  ")
    print("Press 6 for exit  ")
    print("")
    ch = int(input())
    if(ch == 1):
        name = input("Enter fruit name ")
        rate = int(input("Enter fruit rate "))
        if name and rate:
            fruit.append([name,rate])
    elif(ch == 2):
        name = input("Enter the fruit name ")
        for i in fruit:
            if (fruit[fruit.index(i)][0] == name):
                fruit.pop(fruit.index(i))
    elif(ch == 3):
        print("Press 1 for search by name ")
        print("Press 2 for search by rate ")
        print("")
        sch = int(input())
        if (sch == 1):
            name = input("Enter the fruit name ")
            for i in fruit:
                if (fruit[fruit.index(i)][0] == name):
                    print("fruit found in the list ")
                    print (fruit[fruit.index(i)])
        elif (sch == 2):
            rate = int(input("Enter the rate"))
            for i in fruit:
                if (fruit[fruit.index(i)][1] == rate):
                    print("fruit found in the list")
                    print(fruit[fruit.index(i)])
        else:
            print("invalid choice")
    elif(ch == 4):
        name = input("Enter the fruit name ")
        for i in fruit:
            if (fruit[fruit.index(i)][0] == name):
                newn = input("Enter the new name for fruit")
                newr = int(input("Enter the new rate for fruit"))
                fruit[fruit.index(i)][0] = newn
                fruit[fruit.index(i)][1] = newr
                print("updated fruit ", fruit[fruit.index(i)])
    elif(ch == 5):
        print(fruit)
    elif (ch == 6):
        break
    else:
        print("invalid")