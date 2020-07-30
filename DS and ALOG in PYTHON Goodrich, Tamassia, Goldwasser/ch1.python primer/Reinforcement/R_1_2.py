'''Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''

n = int(input('k = '))

def is_even(k):
    if k>=0:
        
        bin_k_str = str(bin(k))
        if bin_k_str[-1]=='0':
            return 'Even'
        else:
            return 'Odd'
    else:
        raise 'Error:number must be positive intiger'

print(is_even(n))
