#!/usr/bin/python3

# print all alphabets in lowercase except q and e

for letter in range(97, 123):
    if letter != 101 and letter != 113:
        print('{}'.format(chr(letter)), end="")
