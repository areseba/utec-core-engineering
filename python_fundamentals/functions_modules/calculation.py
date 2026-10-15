#!/usr/bin/env python3

from calculator_1 import suma, resta, multiplicacion, divicion

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, suma(a, b)))
    print("{} - {} = {}".format(a, b, resta(a, b)))
    print("{} * {} = {}".format(a, b, multiplicacion(a, b)))
    print("{} / {} = {}".format(a, b, divicion(a, b))) 
