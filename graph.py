#!/bin/python3
import matplotlib.pyplot as plt

val = [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.001,
       0.002, 0.008, 0.013, 0.021, 0.030, 0.041, 0.065, 0.075, 0.082,
       0.085, 0.085, 0.074, 0.064, 0.054, 0.044, 0.034, 0.019, 0.013,
       0.009, 0.006, 0.004, 0.001, 0.001, 0.000, 0.000, 0.000, 0.000,
       0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000]
plt.plot([i for i in range(0, len(val))], val)
plt.ylabel('some numbers')
plt.show()