import math

import matplotlib.pyplot as plt
import numpy as np


def getLagger(n, l, x):
    if (n == 1 and l == 0):
        return 1
    if (n == 2 and l == 0):
        return 2 - x
    if (n == 2 and l == 1):
        return 1
    if (n == 3 and l == 0):
        return (6 - 6 * x * x ** 2) / 2
    if (n == 3 and l == 1):
        return 4 - x
    if (n == 3 and l == 2):
        return 1
    if (n == 4 and l == 0):
        return (24 - 36 * x + 12 * x ** 2 - x ** 3) / 6
    if (n == 4 and l == 1):
        return (20 * 10 * x + x ** 2) / 2
    if (n == 4 and l == 2):
        return 6 - x
    if (n == 4 and l == 3):
        return 1


a = 5.3 * 10 ** (-11)  # Водород 0.53 ангстрема
# a = 2.56 * 10 ** (-13)  # Мезоатом водорода 0.00256 ангстрема

# n > 0, l <= n - 1
n = 1
l = 0

x = np.linspace(0, 0.5 * 10 ** -9, 100)

# R(r)
y1 = [math.sqrt(math.factorial(n - l - 1) / (2 * n * math.factorial(n + l))) * (2 / (n * a)) ** (
        l + 3 / 2) * i ** l * math.exp(-i / (n * a)) * getLagger(n, l, (2 * i) / (n * a)) for i in x]
# Пипка не доросла до физики
# 4pir^2*R^2 (r)
y2 = [
    4 * math.pi * i ** 2 * (math.sqrt(math.factorial(n - l - 1) / (2 * n * math.factorial(n + l))) * (2 / (n * a)) ** (
            l + 3 / 2) * i ** l * math.exp(-i / (n * a)) * getLagger(n, l, (2 * i) / (n * a))) ** 2 for i in x]

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x, y1)
# ax1.set(xlabel='$r, 10^{-10} м$')
ax1.set(ylabel='$R(r)$')
ax1.grid()

ax2.plot(x, y2)
# ax2.set(xlabel='$r, 10^{-10} м$')
ax2.set(ylabel='$4{\pi}r^{2}R^{2}(r)$')
ax2.grid()

fig.tight_layout()
plt.show()

