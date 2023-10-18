from contextlib import contextmanager

@contextmanager
def context_string(string_output):
    print("otworzenie managera...\n")

    swapped = string_output.swapcase()
    try:
        yield swapped
    except ValueError as e:
        print('BŁĄD POBORU DANYCH!')
    finally:
        print("\nKONIEC DZIAŁANIA CONTEXT MANAGERA\n")

    print("\n manager zamknięty!")


with context_string('wielkie i ważne wydarzenie dnia: konferencja intellisys 2023') as sws:
    print(sws)
