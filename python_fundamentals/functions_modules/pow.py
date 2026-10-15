#!/usr/bin/env python3

def pow(a, b):
    value = 1
    for i in range(abs(b)):
        value = value * a
    if b < 0:
        return 1 / value
    return value
