def findarrayvalue():
    arr=[102,105,201,150,2001,2000,197]
    value=int(input("type integer to find"))
    if value in arr:
        print('value is found and index number is', (arr.index(value)+1))
    else:
        print('value is not in array')


findarrayvalue()
