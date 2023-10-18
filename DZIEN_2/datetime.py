import datetime
from datetime import time as tm, date
import time

dt_object = datetime.datetime.now()
print(dt_object)

date_object = date.today()
print(date_object)

print(dir(datetime))
print(f"minimalny rok daty: {datetime.MINYEAR}")
print(f"maksymalny rok daty: {datetime.MAXYEAR}")

ts = datetime.date(1966,8,14)
print(f"zadeklarowana data: {ts}")

diff = date_object - ts
print("Różnica czasi.....")
print(diff)
print(f"dolna granica daty: {date.min}")
print(f"górna granica daty: {date.max}")

print(f"data liczona od TS w [s]: {date.fromtimestamp(1385564899)}")

obj = time.gmtime(0)
print(obj)

epoka = time.asctime(obj)
print(epoka)

a = tm(11,54,34,2)
print(f'godzina: {a.hour}')
print(f'minut: {a.minute}')
print(f'sekund: {a.second}')
print(f'mikrosekund: {a.microsecond}')

