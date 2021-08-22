fruit = {}
class Fruits:

    def __init__(self,fid,nm,rt,ifrm,idt,pr):
        self.fid = fid
        self.name = nm
        self.rate = rt
        self.imp_frm = ifrm
        self.imp_date = idt
        self.price = pr

    def display(self):
        print(f"Fruit ID : {self.fid} | Name :  {self.name} | Rate : {self.rate} | From : {self.imp_frm} | Date : {self.imp_date} | Price : {self.price} \n")

def add_fruit():
    fruit_id = int(input("Enter the ID number "))
    if fruit_id not in fruit.keys():
        fid = fruit_id
        name = input("Enter Fruit name ")
        rate = input("Enter Fruit rate ")
        imp_frm = input("Imported from : ")
        imp_date = input("Imported date : ")
        price = input("Buy price : ")
        fruit[fruit_id] = Fruits(fid,name,rate,imp_frm,imp_date,price)
    else:
        print("ID is already taken")

def delete_fruit():
    fname = input("Enter Fruit name ")
    for idn,frt in (fruit.copy()).items():
        if frt.name == fname:
            del fruit[idn]

def search_menu():
    print("Press 1 for search by name ")
    print("Press 2 for search by rate ")
    print("")

def search_name():
    name = input("Enter the fruit name ")
    found = False
    for val in fruit.values():
        if(val.name == name):
            found = True
            val.display()
    if(found == False):
        print("not found")

def search_rate():
    rate = input("Enter the rate")
    found = False
    for val in fruit.values():
        if(val.rate == rate):
            found = True
            val.display()
    if(found == False):
        print("not found")

def change_menu():
    display_fruit()
    print("\n Press 1 for change name")
    print("\n Press 2 for change rate")

def change_name(fruit_id):
    newname = input("Enter new name")
    fruit[fruit_id].name = newname

def change_rate(fruit_id):
    newrate = input("Enter new rate")
    fruit[fruit_id].rate = newrate

def display_fruit():
    for frt in fruit.values():
        frt.display()