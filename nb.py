def negabinary(bits_list):
    result = []

    decimal_value = sum(a * (-2) ** i for i, a in enumerate(bits_list) if a != 0)
    inverted_value = -1 * decimal_value
    print (decimal_value, inverted_value)
    while inverted_value != 0:
        inverted_value, remainder = divmod(inverted_value, -2)
        if remainder < 0:
            inverted_value, remainder = inverted_value + 1, remainder + 2
        result.append(remainder)
   
    return result