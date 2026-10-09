#!/usr/bin/env python3
alphabet = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        alphabet += chr(i)
print("{}".format(alphabet), end="")
