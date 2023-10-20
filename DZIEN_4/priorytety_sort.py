numbers = [8,3,1,2,5,4,7,6,7,2,5,8,6,2]
group = {2,3,5,7}

def sort_prior(values,group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

sort_prior(numbers,group)
print(numbers)
