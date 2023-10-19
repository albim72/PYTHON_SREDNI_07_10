import os

if os.path.exists("bmi.txt"):
    os.remove("bmi.txt")
    print("Plik z danymi archiwalnymi został usunięty!")
else:
    print("plik nie istnieje! Zostanie utworzony nowy!")
