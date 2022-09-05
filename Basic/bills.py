money = int(input("give money amount"))
Fivehundred = 0
Twohundred = 0
Onehundred=0
Ten=0
Fifty=0
Twenty=0
Five = 0
print("Money amount is", money)
for x in range (money):

    if money >= 500:
        Fivehundred +=1
        money = money- 500
    elif money >= 200 and money < 500:
        Twohundred+=1
        money = money-200

    elif money < 200 and money >=100:
        Onehundred +=1
        money = money-100

    elif money < 100 and money >=50:
        Fifty +=1
        money = money-50

    elif money < 50 and money >=20:
        Twenty +=1
        money = money-20

    elif money < 20 and money >=10:
        Ten +=1
        money = money-10
    elif money < 10 and money >=5:
        Five +=1
        money = money-5
       
print(Fivehundred, "Fivehundred euro bills\n" , Twohundred, "Twohundred euro bills\n", Onehundred ,"Onehundred euro bills\n" ,
      Fifty, "Fifty euro bills\n", Twenty, "Twenty euro bills\n",  Ten, "Ten euro bills\n",  Five,"Five euro bills\n", "Left money is", money)
