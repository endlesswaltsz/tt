import datetime

time1=datetime.datetime.now()
time2=datetime.datetime.now()+datetime.timedelta(days=1,hours=3,minutes=3,seconds=33)
print(time2<time1)