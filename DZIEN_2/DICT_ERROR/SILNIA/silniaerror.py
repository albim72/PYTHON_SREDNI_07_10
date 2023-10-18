class SilniaError(Exception):
    def __init__(self,n):
        self.n=n
        
    def __str__(self):
        return (f'[{self.__class__.__name__}] n nie może wynosić: {self.n},'
                f' silnia jest zdefiniowana tylko dla liczb nieujemnych!')
