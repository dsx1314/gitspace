import datetime
import time

dtime = datetime.datetime.now()
un_time = time.mktime(dtime.timetuple())

print(un_time)

times = datetime.datetime.fromtimestamp(un_time)
print(times)
