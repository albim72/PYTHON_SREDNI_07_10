from oblicz import Obliczenia
from daty import Dates


print(f"wartość wynosi: {Obliczenia.moblicz(2,4,8)}")

obl = Obliczenia(1,4,6)
print(obl.moblicz(5,8,2))
print(obl.nsoblicz())

date = Dates("13-12-2019")
dateFDB = "13/12/2019"
dateWithDash = Dates.toDashDate(dateFDB)
print(dateWithDash)

d1 = date.get_date()
d2 = dateWithDash

if(d1==d2):
    print("Identyczne daty")
    print(f"{d1} -- {d2}")
else:
    print("Różne daty")
    print(f"{d1} -- {d2}")
