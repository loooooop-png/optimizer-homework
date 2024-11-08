from scipy.optimize import minimize
import math

# 定义目标函数
def objective_function(x):
    value = 0
    for i in range(0, 10):
        value += (math.exp(x[i])+x[i]**2)
    return value

# 初始猜测
initial_guess = []
for i in range(0, 10):
    initial_guess.append(0.)

# 执行优化
result = minimize(objective_function, initial_guess, method='BFGS')

# 打印结果
print(result)
