import cmath
class Complex:


    def __init__(self,number1,number2):
        self.a=number1;
        self.bi=number2;
     
            
    def setvalues(self,value1,value2):
        self.a=value1
        self.bi=value2
        

    def getvalues(self):
        arvo = complex(self.a,self.bi)
        return arvo



complexobject = Complex(8,-7);
print(complexobject.getvalues());
complexobject.setvalues(2,3)
print(complexobject.getvalues());
