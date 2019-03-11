import math
import time


def average(d):
    compute_with_method(d, lb)


def compute_with_method(d, formula):
    array = []
    start_time = time.time()
    for i in range(0, 50):
        array.append(formula(3500, i, d / 28800))
    print_distribution("Binomial", array, 1 - sum(array[:26]), time.time() - start_time)


def print_distribution(method_name, array, overload, compute_time):
    print("%s distribution:" % method_name)
    tab = ""
    for i in range(0, len(array)):
        print(tab, end="")
        print("%d -> %.3f" % (i, array[i]), end="")
        tab = "\t"
    print("")
    print("overload:  %.1f%%" % (overload * 100))
    print("computation time:  %.2f ms" % compute_time)


def lb(n, k, p):
    proba_ok = pow(p, k)
    proba_ko = pow(1 - p, n - k)
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return proba_ok * proba_ko * comb
