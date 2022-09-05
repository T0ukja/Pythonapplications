class Bird():
    def __init__(self):
 
        print("Bird is ready")


    def setname(self,name):
        self.name=name
        self.eggs = 0;
        print("Name is set as", self.name)
    def getname(self):
        return print("Name is", self.name)
    def seteggs(self,eggs):
        if(eggs <= 10 and eggs >=1):
            self.eggs=eggs
            print("Amount is set")
        else:
            print(eggs, "is too many eggs!")
    def geteggs(self):
        if(self.eggs <= 10 and self.eggs >=1):
            print(self.eggs, "Amount")
        else:
            print("maybe too much eggs?")

lintu = Bird()
lintu.setname("Joe")
lintu.seteggs(13)
lintu.geteggs()
lintu.getname()
