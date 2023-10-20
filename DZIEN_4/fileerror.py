import sys

try:
    f = open("waznedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
except OSError as err:
    print(f"błąd systemowy: {err}")
except ValueError:
    print("nie można przekonwertować str na int")
except Exception as exx:
    print(f"typ klasy obsługującej błąd: {type(exx)}")
    print(exx.args)
    print(exx)
except:
    print(f"nieczekiwany błąd: {sys.exc_info()[0]}")
    raise

