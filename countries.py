import numpy

def writetofile(countrie, pop):
    f = open("countries.txt", "at")
    line = f"{countrie} {pop} \n"
    f.writelines(line)


def read():
    f = open("countries.txt", "r")
    numberarray=[]
    wordarray=[]
    index=0
    for x in f:
            for word in x.split():
                index+=1
                if ',' in word :
                    num1 = word.replace(',','')
                    bignum = int(num1)
                    numberarray.append(bignum)
                else:
                    wordarray.append(word)

    max_value = numpy.argmax(numberarray)       
    print("Biggest population is found at", wordarray[max_value],"and it's population is", max(numberarray))
read()
#writetofile("Finland", "6,000,000")
