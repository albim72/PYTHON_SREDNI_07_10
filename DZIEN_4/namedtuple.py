from collections import namedtuple

Student = namedtuple('Student',['name','age','nr'])
s = Student('Jan Kot','21',4324324)
print(f'student nr {s[2]} --> {s[0]}')
print(f'wiek = {s.age}')
print(f'sesja, student nr {getattr(s,"nr")}')

stdli = ['Olga Nowak',23,423255]
stddic = {'name':'Adam Kowal','age':20,'nr':14343314}
print(f"\ninstancja krotki nazwanej dla listy stdli -> {Student._make(stdli)}")
# sinst = Student._asdict()
print(f"\ninstancja krotki nazwanej dla słownika stddic -> {Student(**stddic)}")

print(f'pola krotki: {Student._fields}')
print(f'krotka po zmianie: {s._replace(name="Maria Niciś")}')
