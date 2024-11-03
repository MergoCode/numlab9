import math

def f(x):
    return math.cos(x)

a = 0
b = 5
n = 50
h = (b - a) / n

with open("input.txt", "w") as file:
    for i in range(n + 1):
        x = a + i * h
        y = f(x)
        file.write(f"{x:.6e}\t{y:.6e}\n")

