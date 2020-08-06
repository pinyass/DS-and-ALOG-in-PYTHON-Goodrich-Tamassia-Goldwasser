'''P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.'''

amt_charged = int(input('Amount charged = '))
amt_paid = int(input('Amount paid = '))
balance = round(amt_paid - amt_charged)
denominations = iter([2000, 500, 200, 100, 50, 20, 10, 5, 2, 1])
def change_generator(bal):
    
