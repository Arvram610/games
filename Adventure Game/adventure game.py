class character:
    def __init__(self):
        self.inventory = []

    def add_item_stackable(self, item_name, amount):

        for i in range(amount):
            item = item_class(item_name)
            self.inventory.append(item)


        print("added {} of item {} to inventory".format(str(amount), item_name))



    def printinv(self):
        printInventory = []
        inventory = []
        for x in self.inventory:
            inventory.append(x.name)

        while len(inventory)!=0:
            printInventory.append(inventory[0]+" : "+str(inventory.count(inventory[0])))
            for i in range(inventory.count(inventory[0])):
                inventory.remove(inventory[0])

        for i in range(len(printInventory)):
            print(printInventory[i])

class item_class:
    def __init__(self, item_name):
        self.name=item_name

p1= character()
p1.add_item_stackable("no", 3)
p1.add_item_stackable("yeet", 1)

p1.printinv()