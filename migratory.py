class migratory():
    def __init__(self):
         print("Migratory")
         self.falsemonth=0
         self.falsecountry=0
    def setmonth(self,month):
        vari = len(month)
        if vari > 1 and vari <12:
            self.month=month
            print("Month is set")
            
        else:
            self.falsemonth=1
            print("Month lenght must be between 5 and 20", "false month name is", month)
            
        
    def setcountry(self,country):
        count = len(country)
        if ((country[0].isupper() == True) and (count >=5 and count <=20 )):
                self.country=country
                print("Country is set")
        else:
            self.falsecountry=1
            print("Country name must be between 5 to 20 letters and it must start with cap\n false name is", country)
    def getmonth(self):
        if(self.falsemonth ==1):
            return print("Month is not applied, apply month again")
        else:
            return print(self.month, "Month")
    def getcountry(self):
        if(self.falsecountry ==1):
            return print("Country is not applied, apply country again")
        else:
            return print(self.country,"Country")

migra = migratory()
migra.setmonth("January")
migra.setcountry("asdsdad")
migra.getmonth()
migra.getcountry()
