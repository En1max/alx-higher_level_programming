#!/usr/bin/python3

# program that prints the ASCII alphabet, in lowercase without  new line

for letter in range(97, 123):
    print('{}'.format(chr(letter)), end="")
