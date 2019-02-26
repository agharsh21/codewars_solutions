import math


def zeros(n):
    prod = 5
    count = 0
    while prod <= n:
        count += math.floor(n / prod)
        prod *= 5

    return count
