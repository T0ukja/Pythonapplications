class User():
    def __init__(self, name, lastname):
        self.name=name
        self.lastname=lastname
        self.children = []
    def owner(self,name):
        self.children.append( Bike( name,self))
        return print(self.name,"Owns a bike, and its name is", name)
    def ownsbike(self):
        return self.children


class Bike(object):
    def __init__(self,name,parent):
        self.name=name
        self.color="white"
    def bikeowner(self):
        return print(self.name)
    def fixbike(self):
        return print("Bike fixed!")
    def customcolor(self,color):
        self.color=color      
    def checkbike(self):
        return print("Bike is checked", "Color of bike is", self.color)


             
pekka = User("Pekka", "Lastname")
pekka.owner("Yosemite")
pekka.ownsbike()[0].bikeowner()
pekka.ownsbike()[0].fixbike()
pekka.ownsbike()[0].checkbike()
pekka.ownsbike()[0].customcolor("Red")
pekka.ownsbike()[0].checkbike()



