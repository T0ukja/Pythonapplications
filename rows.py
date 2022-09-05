print("Give amount of rows")
character="m"
rows=int(input())
for x in range (0,rows):
    print(character)
    character = ''.join((character,'m'))
