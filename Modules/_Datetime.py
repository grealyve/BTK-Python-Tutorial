from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
# result = simdi.year
# result = simdi.month
# result = simdi.day
# result = simdi.hour
# result = simdi.minute
# result = simdi.second

result = datetime.ctime(simdi)
# result = datetime.strftime(simdi, "%Y")
# result = datetime.strftime(simdi, "%X")
# result = datetime.strftime(simdi, "%d")
# result = datetime.strftime(simdi, "%A")
# result = datetime.strftime(simdi, "%B")
# result = datetime.strftime(simdi, "%Y %B %A")
# print(result)

t = "21 April 2019 hour 10:12:30"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
# dt = dt.year

# gun, ay, yil = t.split()
# print(gun)
print(dt)

birthday = datetime(1983,5,9,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds

result = simdi + timedelta(days=10) # şimdi'nin üzerine 10 gün ekler
result = simdi - timedelta(days=730, minutes=10)

print(result)