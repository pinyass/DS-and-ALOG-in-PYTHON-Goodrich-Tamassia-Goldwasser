'''R-1.1  Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.'''

a = int(input('n = '))
b = int(input('m = '))

def is_multiple(n,m):
    if n%m==0:
        return True
    else:
        return False

print(str(is_multiple(a,b)))
