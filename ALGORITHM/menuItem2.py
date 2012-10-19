class Profile:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address
    def show(self):
        print("Name: %s\nAge: %i\nAddress: %s\n" % (self.name, self.age, self.address))
personInfo=[]
person=Profile("Ma. Elvira A. Oco" , 22 , "San Eugenio, Aringay, La Union")
personInfo.append(person)
person=Profile("Jhane Claudette P. Alambra" , 17 , "Rosario, La Union")
personInfo.append(person)
person=Profile("Roberto Jay M. Natividad" , 18 , "Conception, Rosario, La Union")
personInfo.append(person)
person=Profile("Wilmalyn S. Ondoy" , 20 , "Sto. Tomas, La Union")
personInfo.append(person)
person=Profile("John Errol D. Rivera" , 19 , "Nazareno, Agoo, La Union")
personInfo.append(person)
person=Profile("Christian Joy S. Ventura" , 19 , "San Vicente Sur, Agoo, La Union")
personInfo.append(person)
person=Profile("Margarita P. Labid" , 20 , "Casantaan, San Isidro, La Union")
personInfo.append(person)



for person in personInfo:
    person.show()
