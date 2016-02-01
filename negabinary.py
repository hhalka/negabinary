import sys

def from_negabinary(input_vector):
    return sum(a * (-2) ** i for i, a in enumerate(input_vector) if a != 0)

def to_negabinary(quotient):
    digits = []
    while quotient != 0:
        quotient, remainder = divmod(quotient, -2)
        if remainder < 0:
            quotient, remainder = quotient + 1, remainder + 2
        digits.append(str(remainder))
    return ''.join(digits[::-1])

if __name__ == '__main__':
    input_vector = [int(argument) for argument in sys.argv[1:]]
    print ('Input data: {}'.format(input_vector))
    
    decimal_value = from_negabinary(input_vector)
    print ('Decimal value= {}'.format(decimal_value))
    
    inverted_value = -1 * decimal_value
    print ('Inverted value= {}'.format(inverted_value))
    
    print ('Output= {}'.format (to_negabinary(inverted_value)))