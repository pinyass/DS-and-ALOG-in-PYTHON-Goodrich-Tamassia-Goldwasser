'''R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.'''

print(sum(a**2 for a in range(int(input('n = '))) if a%2 != 0))
