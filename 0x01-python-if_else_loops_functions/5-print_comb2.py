#!/usr/bin/python3

# program that prints numbers from 0 to 99 separated by ',' followed by a space

for num in range(99):
    print("{:02d}".format(num), end=", ")
print("99")
