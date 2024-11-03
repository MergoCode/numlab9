import math

def read_m(filename):
    with open(filename, 'r') as input_A:
        lines = input_A.readlines()
        return len(lines) - 1

def power(x, n):
    mult = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        mult *= x
    return mult

def f(x, a, b, m):
    b[m] = a[m]
    for i in range(m - 1, -1, -1):
        b[i] = a[i] + x * b[i + 1]
    return b[0]

def main():
    x0 = 2.51
    eps = 1e-12
    kmax = int(1e4)
    alpha0 = 1.0
    beta0 = 1.0

    m = read_m("input_A.txt")
    print(m)

    with open("input_A.txt", "r") as input_A:
        a = [float(line.strip()) for line in input_A]

    b = [0.0] * (m + 1)
    c = [0.0] * (m + 1)

    print("\nMethod Newton-Gornera")
    x1 = x0
    k = 0
    while True:
        x0 = x1
        b[m] = a[m]
        for i in range(m - 1, -1, -1):
            b[i] = a[i] + x0 * b[i + 1]
        
        c[m] = b[m]
        for i in range(m - 1, 0, -1):
            c[i] = b[i] + x0 * c[i + 1]

        x1 = x0 - b[0] / c[1]
        k += 1
        if k > kmax or (abs(x1 - x0) <= eps and abs(f(x0, a, b, m)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1:.12e}")
        print(f"With iteration {k}")

    with open("output_alg.txt", "w") as output:
        output.write("\nMethod Newton-Gornera\n")
        if k > kmax:
            output.write("Solution not found\n")
        else:
            output.write(f"Solution = {x1:.12e}\n")
            output.write(f"With iteration {k}\n")

    print("\nMethod Lina")
    alpha1 = alpha0
    beta1 = beta0
    k = 0
    while True:
        alpha0 = alpha1
        beta0 = beta1
        p0 = -2 * alpha0
        q0 = alpha0 ** 2 + beta0 ** 2

        b[m] = a[m]
        b[m - 1] = a[m - 1] - p0 * b[m]
        for i in range(m - 2, 1, -1):
            b[i] = a[i] - p0 * b[i + 1] - q0 * b[i + 2]

        q1 = a[0] / b[2]
        p1 = (a[1] * b[2] - a[0] * b[3]) / (b[2] ** 2)
        alpha1 = -p1 / 2
        beta1 = math.sqrt(abs(q1 - alpha1 ** 2))
        k += 1
        if k > kmax or (abs(alpha1 - alpha0) <= eps and abs(beta1 - beta0) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {alpha1:.12e}\t{beta1:.12e}")
        print(f"With iteration {k}")

    with open("output_alg.txt", "a") as output:
        output.write("\nMethod Lina\n")
        if k > kmax:
            output.write("Solution not found\n")
        else:
            output.write(f"Solution = {alpha1:.12e}\t{beta1:.12e}\n")
            output.write(f"With iteration {k}\n")

if __name__ == "__main__":
    main()
