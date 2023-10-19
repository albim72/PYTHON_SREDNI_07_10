import json

jsonsource = '{"imię":"Jan","nazwisko":"Nowak","wiek":50,"miasta":["Zamość","Kraków","Zakopane"]}'

print(jsonsource)
print(type(jsonsource))

osoba = json.loads(jsonsource)
print(osoba)
print(type(osoba))
print(type(osoba["miasta"]))
