#first method

first=3
second=61
third=9
def find3biggest():
    if first > second and first > third:
        print(first,"first is biggest")
    elif second > first and second > third:
        print(second, "second is biggest")
    elif third > first and third > second:
        print(third, "third is biggest")
    else:
        print("some values are same")


#second method
def find3biggestsecond():
    print(max(first,second,third))


find3biggest()
find3biggestsecond()
    
