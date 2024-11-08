import numpy as np
import math
import line_search_methods
import get_gradient
""""
define f(x): e^x1 + x1^2 + e^x2 + x2^2 +...+ e^x10 + x10^2
"""
def f(x):
    value = 0
    for i in range(0, 10):
        value += (x[i]**2 + math.exp(x[i]))
    return value


if __name__=='__main__':
    list = []
    for i in range(0, 10):
        list_=[1.]
        list.append(list_)
    x0 = np.array(list)
    step = 10**(-7)
    x, val, k = line_search_methods.grad_wolfe(f, get_gradient.calculate_one_ways_differential_gradient, x0, step)  # Wolfe准测
    print('步长选择沃夫条件得到的近似最优点：{}\n最优值：{}\n迭代次数：{}'.format(x, val.item(), k))
    alpha = 1
    x, val, k = line_search_methods.grad_trackbacking(f, get_gradient.calculate_analytical_gradient, x0, alpha, 0.25, 0.5, step)#回溯法
    print('步长选择回溯法得到的近似最优点：{}\n最优值：{}\n迭代次数：{}'.format(x, val.item(), k))
    alpha = 0.5
    x, val, k = line_search_methods.grad_constant_step(f, get_gradient.calculate_analytical_gradient, x0, alpha, step)#固定步长法
    print('步长选择固定步长法得到的近似最优点：{}\n最优值：{}\n迭代次数：{}'.format(x, val.item(), k))
    get_gradient.draw_one_way_differential_gradient(f, x0)
    """
    显示step取10^(-7)时，误差最小
    """