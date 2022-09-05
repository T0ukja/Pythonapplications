x=True
amount=0.0
while x==True:
    print("\nMenu \nPress 1 to do deposit\nPress 2 to check balance\nPress 3 to do withdrawal\n")
    inppu=int(input())
    if inppu ==1:
        print("make deposit")
        deposit=float(input())
        if deposit >0:
            amount +=deposit
            print("Success")
        else:
            print("false input")
        
    if inppu == 2:
        print("Check balance")
        print("Balance is",amount)
    if inppu == 3:
        print("Do withdrawal")
        withdrawal=float(input())
        if withdrawal <= amount:
            amount -=withdrawal
            print("Success")
        else:
            print("There is not enough money in your bank account")

    

    
