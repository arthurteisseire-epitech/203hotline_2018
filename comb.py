import math


def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
