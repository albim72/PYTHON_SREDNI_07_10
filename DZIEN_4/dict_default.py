from collections import defaultdict

def log_missing():
    print('Klucz został dodany')
    return 0

current = {'zielony':12,'niebieski':4}
increments = [
    ('czerwony',5),
    ('niebieski',17),
    ('pomarańczowy',9)
]

result = defaultdict(log_missing,current)
print('Przed: ', dict(result))

for key,amount in increments:
    result[key] += amount

print('Po: ', dict(result))
