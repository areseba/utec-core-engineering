#!/usr/bin/env python3

def uppercase(str):
    cadena = ""
    for i in str:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            cadena += chr(ord(i) - 32)
        else:
            cadena += i
    print(cadena)
