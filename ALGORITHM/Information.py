class Information:
    def __init__(self,fullname,hometown,age):
        self.fullname=fullname
        self.hometown=hometown
        self.age=age
    def show(self):
        print("Your Fullname is %s.You are from  %s.You are %i years old." % (self.fullname,self.hometown,self.age))

InformationAboutYou=[]
info=Information("Jane Claudette Alambra","Bacani,Rosario,La Union",17)
InformationAboutYou.append(info)
info=Information("Sony Valdez","Agoo,La Union",27)
InformationAboutYou.append(info)
info=Information("Wilmalyn Ondoy","Namboongan,Sto.Tomas,La Union",20)
InformationAboutYou.append(info)
info=Information("Christian Joy Ventura","San Vicente Sur,Agoo,La Union",19)
InformationAboutYou.append(info)
info=Information("John Errol Rivera","Nazareno,Agoo,La Union",19)
InformationAboutYou.append(info)

for info in InformationAboutYou:
    info.show()
