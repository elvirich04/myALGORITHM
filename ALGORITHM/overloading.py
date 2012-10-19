class Clock:
    def Time(self):
        print("Clock Says 6:00")

class WallClock(Clock):
    def Time(self):
        print("The wall clock says 6:00")

class WristWatch(Clock):#parent of Rolex
    def Time(self):
        print ("The wrist watch says 6:00")

class Rolex(WristWatch):
    def Time(self):
        print ("The expensive Rolex says 6:00")

class FakeRolex(Rolex):
    def Time(self):
        Clock.Time(self)#can be changeable for the results of the parents
        
watch=FakeRolex()#instance, w/c will run the program
watch.Time()
