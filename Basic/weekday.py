
day = input("Give day")

def monday():
    return "Monday"
def tuesday():
    return "Tuesday"
def wednesday():
    return "Wednesday"
def thursday():
    return "Thursday"
def friday():
    return "Friday"
def saturday():
    return "Saturday"
def sunday():
    return "Sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(day):
    return switcher.get(day, default)()
print("The Number you entered is", day, "and the weekday for that number is", switch(int(day)))



