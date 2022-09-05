import time

class Clock:
    def __init__(self):
        print("Clock is ready")

    def ticking(self):
        return print("Clock is ticking")

    
    class AlarmClock:
        def __init__(self):
            #value = 0
            #self.alarmvalue = value;
            print("This is alarmclock")

        def setalarm(self,value):
            self.alarmvalue = value;
            print("Alarm is set to start at", self.alarmvalue, " seconds")
            if(self.alarmvalue !=0):
                while (self.alarmvalue !=0):
                    print(self.alarmvalue, "Seconds left")
                    self.alarmvalue -=1;
                 
                    time.sleep(1)
                print("Alarm is set to start now, peep peep peep!")

clock = Clock()
print(clock.ticking())
clockk = clock.AlarmClock()
clockk.setalarm(5)

        
