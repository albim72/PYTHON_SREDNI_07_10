class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped = skipped
        return instance

postp = PositiveTuple(0,4,-5,2,-19,14,5,0,345,-122)
print(postp)
print(type(postp))
print(postp.skipped)
