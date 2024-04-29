#!/bin/usr/python3
if __name__ == "__main__":
    from sys import argv
num1 = 0
lenght = len(argv)
for i in range(1, lenght):
    num1 += int(argv[i])
print('{}'.format(num1))
