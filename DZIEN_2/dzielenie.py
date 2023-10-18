def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("nie dziel przez 0!!!")
    except NameError as ne:
        print(ne)
    except TypeError as te:
        print(te)
    except Exception as exc:
        print(exc)
    else:
        print(f'wynik = {wynik}')
    finally:
        print("policzmy coś jeszcze...")

try:
    dzielenie(4,5)
    dzielenie(4,0)
    dzielenie(0,0)
    dzielenie(0.1,0.000000034)
    dzielenie(-88.7,1.99999)
    dzielenie(False,6)
    dzielenie(4,True)
    dzielenie("ffgsdfs",9)
    dzielenie(45)
except TypeError as t:
    print(t)
