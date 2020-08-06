'''P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.'''

def permutations(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i+1:]
            for p in permutations(remLst):
                l.append([m]+p)
        return l

data = list('catdog') 
for p in permutations(data): 
    print(p)
