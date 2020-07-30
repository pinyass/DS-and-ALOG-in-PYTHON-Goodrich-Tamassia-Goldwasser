'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''

n = int(input('a = '))

def sum_odd_square(a):
    sum_number = 0
    for i in range(a):
        if i%2!=0:
            sum_number += i**2
    return sum_number

print(sum_odd_square(n))
