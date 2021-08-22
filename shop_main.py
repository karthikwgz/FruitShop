import fruit
import display_buy as b


print("__________Fruit Shop ___________")

def fruit_menu():
    print("\n1. Add fruit \t2. Delete fruit \t3. Search fruit by name and rate")
    print("4. Change fruit name and rate \t5. Display and buy \t6.disp exit")
    print("\n_____________________________________\n")

while True:
    fruit_menu()
    ch = int(input())
    if(ch == 1):
        fruit.add_fruit()
    elif (ch == 2):
        fruit.delete_fruit()
    elif(ch == 3):
        fruit.search_menu()
        sch = int(input())
        if (sch == 1):
            fruit.search_name()
        elif (sch == 2):
            fruit.search_rate()
        else:
            print("invalid choice")
    elif(ch == 4):
        fruit_id = int(input("Enter id"))
        if fruit_id not in fruit.fruit.keys():
            print("invalid id")
        else:
            fruit.change_menu()
            cho = int(input("Enter choice"))
            if(cho == 1):
                fruit.change_name(fruit_id)
            elif (cho == 2):
                fruit.change_rate(fruit_id)
                
    elif(ch == 5):
        b.display_buy()
    elif(ch == 6):
        fruit.display_fruit()
    elif (ch == 7):
        break
    else:
        print("invalid")