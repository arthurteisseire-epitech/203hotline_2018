import math


def average(d):
    array = []
    for i in range(0, 50):
        array.append(lb(i, 3500, d / 28800))
    print_distribution("Binomial", array, 0, 0)


def print_distribution(method_name, array, overload, compute_time):
    print("%s distribution:" % method_name)
    tab = ""
    for i in range(0, len(array)):
        print(tab, end="")
        print("%d -> %.3f" % (i, array[i]), end="")
        tab = "\t"
    print("")
    print("overload:  %.1f%%" % overload)
    print("computation time:  %.2f ms" % compute_time)


def lb(n, k, p):
    if k > n:
        return 0
    proba_ok = pow(p, k)
    proba_ko = pow(1 - p, n - k)
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return proba_ok * proba_ko * comb
