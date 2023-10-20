liczby = [56,57,89,90,62,87,87,91,89,76,75,51,77,78,90,84,81,79,78,92]

def get_srednia_odchyl(dane):
    average = sum(dane)/len(dane)
    skalowanie = [x/average for x in dane]
    skalowanie.sort(reverse=True)
    return skalowanie

longest,*middle,shortest = get_srednia_odchyl(liczby)
print(f'największa wartość: {longest:0.0%} średniej')
print(f'najmniejsza wartość: {shortest:0.0%} średniej')
