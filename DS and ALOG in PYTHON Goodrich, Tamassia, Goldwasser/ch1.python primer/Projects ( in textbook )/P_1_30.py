'''P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.'''

number = int(input('number = '))
count = 0
if number > 2:
    while True:
        rem = number/2
        count += 1
        number = rem
        if rem<2.0:
            break
else:
    print('enter a positive number greater than 2')
    

print('\nNumbre of times number needs to be divided by 2 to get a number smaller than 2 : ',count)
