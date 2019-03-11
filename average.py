def average(d):
    pass


def print_distribution(method_name, array, overload, compute_time):
    print("%s distribution:", method_name)
    tab = ""
    for i in range(0, len(array)):
        print(tab, end="")
        print("%d -> %.3f" % (i, array[i]))
        tab = "\t"
    print("overload:  %.1f%%", overload)
    print("computation time:  %.2f ms", compute_time)

