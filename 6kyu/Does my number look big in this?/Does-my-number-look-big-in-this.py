import math


def narcissistic(value):

    number = list(str(value))
    power = len(number)
    num = 0
    for n in range(power):
        num = num + math.pow(int(number[n]), power)
    if num == value:
        return True
    else:
        return False
