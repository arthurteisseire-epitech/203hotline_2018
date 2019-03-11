import math


def compute(n, k):
    if k > n:
        exit(84)
    print("%d-combination of a %d set:\n%d" % (k, n, comb(n, k)))


def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
