'''C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.'''
import time

n = int(input('n = '))
lst = [a for a in range(n)]
print(lst)
t1 = time.time()
length = int((len(lst)/2))
for i in range(length):
    lst[i],lst[-i-1] = lst[-i-1],lst[i]
t2 = time.time()
print(lst)
print(float(t2-t1))
