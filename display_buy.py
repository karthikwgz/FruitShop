from fruit import fruit


cart = []

def add_to_cart():
    for key,val in fruit.items():
        print(key,"." ,val.name)
    id = int(input("Enter fruit id"))
    cart.append(fruit[id])

def display_cart():
    for i in cart:
        i.display()
def delete_from_cart():
    display_cart()
    idn = int(input("Enter the fruit id"))
    for i in cart:
        if i.fid == idn:
            cart.pop(cart.index(i))
def bill():
    print("\n___________________________Bill______________________________")
    for i in cart:
        i.display()
    print("\tThank you\n")

def display_buy():
    while True:
        print("1. Add to cart \t 2. Delete from cart \t 3.Bill")
        print("4. Display cart \t 6 exit")
        ch = int(input("Enter the choice"))
        if (ch == 1):
            add_to_cart()
        elif (ch == 2):
            delete_from_cart()
        elif (ch == 3):
            bill()
        elif (ch == 4):
            display_cart()
        elif(ch == 6):
            break
        else:
            print("invalid option")