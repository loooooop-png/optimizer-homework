import numpy as np
import math
"""
fun is the function to be optimized
gfun is the gradient of fun
x0 is the initial point
step is the step size
alpha is the step size factor
c is the constant in the Wolfe condition
t is the constant in the backtracking method
"""
def grad_wolfe(fun, gfun, x0, step): # 使用wolfe准则来求步长因子的最速下降法
    maxk = 5000
    k = 0
    epsilon = 1e-5
    while k < maxk:
        gk = gfun(x0, fun, step)
        dk = -gk
        if np.linalg.norm(dk) < epsilon:#norm:计算范数
            break
        rho = 0.4
        sigma = 0.5
        a = 0
        b = np.inf
        alpha = 1
        while True:
            if not ((fun(x0) - fun(x0 + alpha * dk)) >= (-rho * alpha * gfun(x0, fun ,step).T @ dk)):#@:矩阵乘法
                b = alpha
                alpha = (a + alpha) / 2
                continue
            if not (gfun(x0 + alpha * dk, fun, step).T @ dk >= sigma * gfun(x0, fun, step).T @ dk):
                a = alpha
                alpha = np.min([2 * alpha, (alpha + b) / 2])
                continue
            break

        x0 = x0 + alpha * dk
        k += 1
    x = x0
    val = fun(x)
    return x, val, k

def grad_constant_step(fun, gfun, x0, alpha, step):#使用定值步长的最速下降法
    maxk =5000
    k = 0
    epsilon = 1e-5
    while k < maxk:
        gk = gfun(x0, fun, step)
        dk = -gk
        if np.linalg.norm(dk) < epsilon:
            break
        x0 = x0 + alpha * dk
        k += 1
    x = x0
    val = fun(x)
    return x, val, k

def grad_trackbacking(fun, gfun, x0, alpha_, c, t, step):
    maxk = 5000
    k = 0
    epsilon = 1e-5
    ministep = 1e-5
    flag = False
    while k < maxk:
        gk = gfun(x0, fun, step)
        dk = -gk
        alpha = alpha_
        if np.linalg.norm(dk) < epsilon:
            break
        while True:
            if not (fun(x0 + alpha * dk) <= fun(x0) + c * alpha * gfun(x0, fun, step).T @ dk):
                if np.linalg.norm(alpha * dk) <= ministep:
                    flag = True
                    break
                alpha = alpha * t
                continue
            break
        if flag:
            break
        x0 = x0 + alpha * dk
        k += 1
    x = x0
    val = fun(x)
    return x, val, k