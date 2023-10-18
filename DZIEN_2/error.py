try:
    print(x)
except NameError:
    print("x nie jest zdefiniowany!")
except TypeError as tp:
    print(tp)
except Exception as exc:
    print(exc)
else:
    print(f'2*x = {2*x}')
finally:
    y=9
    print(f'składowa y = {y}')


print("ciąg dalszy.....")

