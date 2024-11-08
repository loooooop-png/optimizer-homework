import numpy as np
import math
import matplotlib.pyplot as plt
"""
x is the point to be calculated
f is the function to be optimized
step is the step size
"""
def calculate_analytical_gradient(x, f, step):
    list = []
    for i in range(0, 10):
        list.append(math.exp(x[i]) + 2*x[i])
    return np.array(list)


def calculate_one_ways_differential_gradient(x, f, step):
    d = step
    list = []
    for i in range(0, 10):
        x[i][0] += d
        y1 = f(x)
        x[i][0] -= d
        y2 = f(x)
        value = (y1 - y2) / d
        list.append(value)
    return np.array(list)

def calculate_double_way_differential_gradient(x, f, step):
    #d = 0.001
    d = step
    list = []
    for i in range(0, 10):
        x[i][0] += d
        y1 = f(x)
        x[i][0] -= (2*d)
        y2 = f(x)
        x[i][0] += d
        value = y1 - y2
        value /= (2*d)
        list.append(value)
    return np.array(list)

def draw_one_way_differential_gradient(f, x0):
    x = x0
    x_label = []
    y_label = []
    for i in range(1, 11):
        val = np.linalg.norm(calculate_one_ways_differential_gradient(x, f, 10**(-i)) - calculate_analytical_gradient(x, f, 10**(-i)))
        val /= np.linalg.norm(calculate_analytical_gradient(x, f, 10**(-i)))
        x_label.append(-i)
        y_label.append(math.log(val))
    print(x_label)
    print(y_label)
    plt.plot(x_label, y_label)
    plt.xlabel('log(epison)')
    plt.ylabel('log(relative error)')
    plt.grid(True)
    plt.gca().invert_xaxis()
    plt.show()
