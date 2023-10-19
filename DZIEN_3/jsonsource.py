import json

jsonsource = '{"imię":"Jan","nazwisko":"Nowak","wiek":50,"miasta":["Zamość","Kraków","Zakopane"]}'

print(jsonsource)
print(type(jsonsource))

osoba = json.loads(jsonsource)
print(osoba)
print(type(osoba))
print(type(osoba["miasta"]))

pojazd = {
    "marka":"Jeep",
    "model":"Cherokee",
    "rocznik":2020,
    "poj":4.8,
    "kategoria":{
        "nazwa":"SUV",
        "mocmin":170,
        "cenamin":125900
    }
}

print(pojazd)
jsonpojazd = json.dumps(pojazd,indent=4)
print(jsonpojazd)
print(type(jsonpojazd))

class Pojazd:
    def __init__(self,marka,model,rocznik):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik

p = Pojazd("Fiat","Freemont",2016)
pjson = json.dumps(p.__dict__)

print(pjson)

with open("pojazd.json","w",encoding="utf-8") as f:
    f.write(jsonpojazd)


with open("pojazd.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)


