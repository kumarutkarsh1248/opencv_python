
def int_roman(x):
    roman_template = {
        3000: 'MMM',  
        2000: 'MM',  
        1000: 'M', 
        900: 'CM',
        500: 'D',
        400: 'CD', 
        300: 'CCC',
        200: 'CC',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        30: 'XXX',
        20: 'XX',  
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        3: 'III',
        2: 'II',
        1: 'I'
    }
    roman_list = []
    
    for element in roman_template:
        if element <= x:
            x = x % element
            roman_list.append(1)
        else:
            roman_list.append(0)

    return roman_list

    # roman_numeral =""

    # for index, element in enumerate(roman_template):
    #     if roman_list[index] == 1:
    #         roman_numeral += roman_template[element]
    # return roman_numeral




def roman_to_integer(s):
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    for char in reversed(s):
        current_value = roman_to_int[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total


for i in range(1000):
    print(int_roman(i))
