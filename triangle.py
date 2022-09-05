A = float(input("Give lenght of triangle side A"))
B = float(input("Give lenght of triangle side B"))
C = float(input("Give lenght of triangle sides C"))
lista = {'A':A,'B':B,'C':C}
arvo = (max(lista, key=lista.get))
sa = pow(A, 2)
sb = pow(B, 2)
sc = pow(C, 2)
def check():
        if A==B or B==C or C==A:
            print("Isosceles triangle")
        elif (sa > sc + sb or sb > sa+sc or sc > sa+sb):
                print("Obtuse-angled triangle")
        elif A==B and B==C and C==A:
            print("Equilateral Triangle")
        elif A!=B and B!=C and C!=A:
            print("Scalene triangle")
        else:
                print("Acute-angled triangle")


if (arvo == 'A'):
	if (C**2 + B**2 == A**2):
		print("Triangle is Right Angled")
	else:
		check()
if(arvo == 'B'):
	if(C**2 + A**2 == B**2):
		print("Triangle is Right Angled")
	else:
		check()

# If c is largest side of triangle
if(arvo == 'C'):
	if(A**2 + B**2 == C**2):
		print("Triangle is Right Angled")
	else:
		check()
            
    

