1.Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]

def reduce_fraction(fraction):
    print(min(fraction))
    nok = 1
    for i in range(1, min(fraction)+1):
        if fraction[0]%i == 0 and fraction[1]%i == 0:
            nok = i
    print(nok)

    return fraction[0]//nok, fraction[1]//nok


