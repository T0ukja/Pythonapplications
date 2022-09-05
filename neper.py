
def neper():
    e = f = 1.0
    for i in range(2, 16):
        e += 1.0 / f
        f *= i
    print(e)


neper()
