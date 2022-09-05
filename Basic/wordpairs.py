arr=[]

i=0

howmany= int(input("how many dictionary words do you wanna add?"))
while i != howmany:
    i +=1
    print(i, "Wordpair")
    finword=input("add finnish word")
    engword=input("add english word")
    arr.append(finword+"-"+engword)
   
   


print(arr)
