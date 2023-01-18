#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n1 = str(number)
digit = n1[-1]
digit = int(digit)
if number < 0:
    if digit > 5:
        print(f"Last digit of {n1} is -{digit} and is greater than 5")
    elif digit == 0:
        print(f"Last digit of {n1} is {digit} and is zero")
    elif digit < 6 and digit != 0:
        print(f"Last digit of {n1} is -{digit} and is less than 6 and not 0")
else:
    if digit > 5:
        print(f"Last digit of {n1} is {digit} and is greater than 5")
    elif digit == 0:
        print(f"Last digit of {n1} is {digit} and is zero")
    elif digit < 6 and digit != 0:
        print(f"Last digit of {n1} is {digit} and is less than 6 and not 0")
