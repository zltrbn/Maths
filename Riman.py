import numpy as np
import matplotlib.pyplot as plt
import math
import random

def f(x):
    return math.e**(2*x)
def g(x):
    return np.sin(2*x)
def h(x):
    return 2 ** x

def draw(f, a, b, n, equipment):
    x = np.linspace(a, b, n)
    y = f(x)
    plt.plot(x, y, 'b')
    summa = 0
    for i in range(n - 1):
        x_i = x[i]
        x_i_plus_1 = x[i + 1]
  
        if equipment == "left":
            j = x_i
        elif equipment == "middle":
            j = (x_i + x_i_plus_1) / 2
        elif equipment == "right":
            j = x_i_plus_1
        else:
            j = random.uniform(x_i, x_i_plus_1)
        plt.fill_between([x_i, x_i_plus_1], [0, 0], [f(j), f(j)], color='red', alpha=0.3)
        summa += f(j) * (b - a) / n
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral Sums')
    plt.show()
    return summa


print("1. f(x) = e^(2x)")
print("2. f(x) = sin(2x)")
print("3. f(x) = 2^x")
number = int(input("Введите номер функции, интегральную сумму которой вы хотите найти: "))
functions = [f, g, h]
function = functions[number - 1]
n = int(input("Введите n: "))
a, b = map(int, input("Введите a и b (через пробел): ").split())
equipment = input("Введите оснащение (\"left\" - левые точки; \"right\" - правые точки; \"middle\" - средние точки; \"random\" - случайные точки): ")
print(draw(function, a, b, n, equipment))
plt.show()

draw(f)
print(sq(f))