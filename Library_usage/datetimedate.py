import datetime
import pytz
datem = datetime.datetime.now()
timezone = pytz.timezone("Europe/Amsterdam")
datem = timezone.localize(datem)
datem.tzinfo

print("example value is", datem)
print(datem.day, "day")      
print(datem.month, "month")    
print(datem.year, "year")       
print(datem.hour, "hour")       
print(datem.minute, "Minute")     
print(datem.second, "seconds")     
print(datem.microsecond, "microseconds")


