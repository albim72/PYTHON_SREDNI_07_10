#budowa słownika poprzez zadanie listy lub krotki z kluczami i wartościami
#wartości słownika mogą przyjmować tylko 2 typy: int oraz float

from derrors import KeyValueConstructError, IntFloatValueError

class CustomInFloatDict(dict):
    empty_dict = {}

    def __init__(self, key=None, value = None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float)):
                    raise IntFloatValueError(val)
                dict.__setitem__(self,k,val)

    def get_dict(self):
        return self.empty_dict

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise IntFloatValueError(value)
        return dict.__setitem__(self,key,value)

test_1 = CustomInFloatDict()
print(test_1)
print(type(test_1))

# test_2 = CustomInFloatDict({'a','b'},[4,7])
# print(test_2)

# test_3 = CustomInFloatDict(('x','y','z'),(10,"twenty",30))
# print(test_3)

test_4= CustomInFloatDict(('x','y','z'),(10,20,30))
print(test_4)
