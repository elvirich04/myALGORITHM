class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show(self):
        print(self.name)
        print(".........................%f " % (self.price))
MenuItemCollection=[]
item=MenuItem("Spaghetti",49.00)
MenuItemCollection.append(item)
item=MenuItem("Palabok",25.50)
MenuItemCollection.append(item)
item=MenuItem("Softdrink",12.00)
MenuItemCollection.append(item)
item=MenuItem("Pancit",10.00)
MenuItemCollection.append(item)
item=MenuItem("Coke Float",25.00)
MenuItemCollection.append(item)
item=MenuItem("Budget Meal",25.00)
MenuItemCollection.append(item)
item=MenuItem("ExtraRice",7.00)
MenuItemCollection.append(item)
item=MenuItem("Meat",25.00)
MenuItemCollection.append(item)
item=MenuItem("Vegetable",10.00)
MenuItemCollection.append(item)
item=MenuItem("Burger Steak",20.00)
MenuItemCollection.append(item)
item=MenuItem("Hotdog",15.00)
MenuItemCollection.append(item)

for item in MenuItemCollection:
    item.show()
