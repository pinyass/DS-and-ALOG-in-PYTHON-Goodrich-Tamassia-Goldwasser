'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.'''

n = int(input('k = '))

def square_sum(n):
    if n>1:
        sum_of_square = 1
        for i in range(2,n):
            sum_of_square += i**2
        return sum_of_square
    elif n == 1:
        return 1
    else:
        raise 'Error : number must be an intiger greater than zero'

print(square_sum(n))
