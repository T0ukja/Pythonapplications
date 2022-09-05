def biggest():
    first=int(input("Give first value"))
    second=int(input("Give second value"))
    third=int(input("Give third value"))
    fourth=int(input("Give fourth value"))
    fifth=int(input("Give fitfh value"))
    arr=[first,second,third,fourth,fifth]
    print("max value is", max(arr), "and it is", (1+(arr.index(max(arr)))), "number")

biggest()
