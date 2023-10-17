liczby = [56,90,88,100,-45,0,194,999,-1998,2104,188,-34,-100,123456,901,-564,2,5,6]

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    sr_arytm = suma_el/liczba_el
    return minimum,maksimum,rozstep,liczba_el,sr_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini, maxi, roz, le, sa = pokaz_statystyki(liczby)
print(f"wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp wartości: {roz},"
      f"liczba elementów: {le}, średnia arytmetyczna: {sa}")
