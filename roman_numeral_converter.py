def number_to_roman(number):
    numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    roman = ""
    for value, numeral in numerals.items():
        while number >= value:
            roman += numeral
            number -= value
    return roman

to_be_converted = int(input("Enter a number: \n"))
print("Roman numeral equivalent: \n" + number_to_roman(to_be_converted))