seconds = int(input("Give seconds"))


if seconds >= 3600:
    Fulltime = seconds / 3600
    Hours = int(Fulltime)
    Minutes = int((Fulltime - Hours)*60)
    Seconds = round((((Fulltime - Hours)*60)-Minutes)*60)
    print("Hours", Hours, "Minutes", Minutes, "and", Seconds, "seconds")
if seconds < 3600 and seconds > 60:
    Fulltime = seconds / 3600
    Hours = int(Fulltime)
    Minutes = int((Fulltime - Hours)*60)
    Seconds = round((((Fulltime - Hours)*60)-Minutes)*60)

    print("Minutes", Minutes, "and", Seconds, "seconds")
else:
    Fulltime = seconds / 3600
    Hours = int(Fulltime)
    Minutes = int((Fulltime - Hours)*60)
    Seconds = round((((Fulltime - Hours)*60)-Minutes)*60)
    print("Seconds", seconds)
