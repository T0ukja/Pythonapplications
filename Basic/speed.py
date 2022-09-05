Speed = float(input("Give speed of car km/h "))
Distance = float(input("Give distance (km) "))

TimeHours = Distance/Speed
WholeTimeH = int((Distance/Speed))
WholeTimeM = (TimeHours - WholeTimeH)*60
if TimeHours >= 1:
    print("Time in hours is", TimeHours)
    print(" Time in hours is", WholeTimeH, "And", WholeTimeM, "Minutes")


else:
    print(" Time in Minutes is", WholeTimeM)




