import numpy
def writetofile(countrie, pop):
        try:
         f = open("countries.txt", "at")
        except Exception as exc:
            print("Cannot open file:", exc)
        try:
         line = f"{countrie} {pop} \n"
         f.writelines(line)
        except Exception as exc:
           print("error occured", exc)
           
def read():
        try:
            f = open("countriess.txt", "r")
            numberarray=[]
            wordarray=[]
            index=0
        except IOError as e:
                print("error occured while opening", e)
        try:
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
            print("Biggest population is found at", wordarray[max_value]," and it's population is", max(numberarray))
        except Exception as exc:
                print("error occured while opening", exc)
read()
#writetofile("Finland", "6,000,000")
