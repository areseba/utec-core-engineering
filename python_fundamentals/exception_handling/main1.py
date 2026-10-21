#!/usr/bin/env python3

safe_print_integer = __import__('safe_print_integer').safe_print_integer

print("Prueba con un entero:")
resultado = safe_print_integer(10)
print(resultado)

print("Prueba con un texto:")
resultado = safe_print_integer("hola")
print(resultado)