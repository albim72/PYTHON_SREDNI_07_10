import json

def dodaj_nowego_pracownika(new_data,filename="pracownik.json"):
    with open(filename,"r+",encoding="utf-8") as file:
        file_data = json.load(file)
        file_data["pra_info"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)


nowyprac = {
            "imie": "Benek",
            "nazwisko": "Knot",
            "stanowisko": "kierowca",
            "lata_pracy": 4,
            "email": "benek@firma.pl"
        }

dodaj_nowego_pracownika(nowyprac)
