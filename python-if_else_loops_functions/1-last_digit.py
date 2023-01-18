#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
digit = int(str(abs(i))[-1])
if number < 0:
    if digit != 0:
        print(f"Last digit of {i} is -{digit} and is less than 6 and not 0")
    elif digit == 0:
        print(f"Last digit of {i} is {digit} and is 0")

else:
    if digit > 5:
        print(f"Last digit of {i} is {digit} and is greater than 5")
    elif digit == 0:
        print(f"Last digit of {i} is {digit} and is 0")
    elif digit < 6 and digit != 0:
        print(f"Last digit of {i} is {digit} and is less than 6 and not 0")
