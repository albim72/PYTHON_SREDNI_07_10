import csv

with open("firma.csv",encoding="utf-8") as pc:
    csv_reader = csv.reader(pc,delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'NAZWA KOLUMNY: {", ".join(row)}')
            line_count += 1

        else:
            print(f'\t{row[0]} pracuje na stanowisku {row[1]} i ma urodziny w miesiącu: {row[2]}. '
                  f'otrzymuje nagrodę finansową w wysokości: {row[3]} zł')
            line_count += 1

    print(f"liczba dodanych linii: {line_count}")
    print(f"liczba dodanych osób: {line_count-1}")


with open("emp_file.csv",'w',encoding='utf-8') as ef:
    emp_writer = csv.writer(ef,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONE, lineterminator="\n")
    emp_writer.writerow(('imię i nazwisko','Dział','miesiąc'))
    emp_writer.writerow(('Jan Kosak','Zarząd','luty'))
    emp_writer.writerow(('Anna Kot','Finanse','czerwiec'))
    emp_writer.writerow(('Nasia Wrzos','Dział','miesiąc'))
