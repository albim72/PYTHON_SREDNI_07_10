import shutil

s = "tekst do wyśrodkowanie"

def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))
print_center(s)
