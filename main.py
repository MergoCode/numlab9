import math

# Define the function and its derivatives
def f(x):
    return math.cos(x)

def fp1(x):
    return -math.sin(x)

def fp2(x):
    return -math.cos(x)

# Power function
def power(x, n):
    if n == 0:
        return 1.0
    result = 1.0
    for _ in range(n):
        result *= x
    return result

# Simple Iteration Method
def Simple_Iteration(kmax, eps, x0):
    print("\nMethod: Simple Iteration")
    tau = -1 / fp1(x0)
    x1 = x0
    for k in range(kmax):
        x0 = x1
        x1 = x0 + tau * f(x0)
        if abs(x1 - x0) <= eps or abs(f(x1)) <= eps:
            print(f"Solution = {x1}\nWith iteration {k + 1}")
            return x1, k + 1
    print("Solution not found")
    return None, kmax

# Newton's Method
def Method_Newton(kmax, eps, x0):
    print("\nMethod: Newton")
    x1 = x0
    for k in range(kmax):
        x0 = x1
        x1 = x0 - f(x0) / fp1(x0)
        if abs(x1 - x0) <= eps or abs(f(x1)) <= eps:
            print(f"Solution = {x1}\nWith iteration {k + 1}")
            return x1, k + 1
    print("Solution not found")
    return None, kmax

# Chebyshev Method
def Method_Chebysheva(kmax, eps, x0):
    print("\nMethod Chebysheva")
    x1 = x0
    k = 0
    tau = -1.0 / fp1(x0)
    while True:
        x0 = x1
        x1 = x0 - f(x0) / fp1(x0) - 0.5 * power(f(x0), 2) * fp2(x0) / power(fp1(x0), 3)
        k += 1
        if k > kmax or abs(x1 - x0) <= eps or abs(f(x1)) <= eps:
            break
    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1}")
        print(f"With iteration {k}")
    return x1, k

# Secant Method
def Method_Hord(kmax, eps, x0):
    print("\nMethod Hord")
    x1 = x0 + 0.1  # Initial guess for x1
    tol = 1e-10    # Tolerance for zero check
    k = 0
    
    while True:
        denominator = f(x1) - f(x0)
        if abs(denominator) < tol:
            print("Denominator is too small, stopping iteration to avoid division by zero.")
            break
        
        x2 = x1 - f(x1) * (x1 - x0) / denominator
        k += 1
        
        if k > kmax or abs(x2 - x1) <= eps or abs(f(x2)) <= eps:
            break

        x0, x1 = x1, x2
    
    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x2}")
        print(f"With iteration {k}")
    return x2, k

# Parabolic Method
def Method_Parabol(kmax, eps, x0):
    print("\nMethod: Parabolic")
    tau = -1 / fp1(x0)
    x1 = x0 + tau * f(x0)
    x2 = x1 + tau * f(x1)
    x3 = x2
    for k in range(kmax):
        rr1 = (f(x2) - f(x1)) / (x2 - x1)
        rr2 = ((f(x2) - f(x1)) / (x2 - x1) - (f(x1) - f(x0)) / (x1 - x0)) / (x2 - x0)
        
        root_term = power((x2 - x1) * rr2 + rr1, 2) - 4 * rr2 * f(x2)
        if root_term < 0:
            print("Complex roots encountered, stopping iteration.")
            break

        root = math.sqrt(root_term)
        delta1 = (-((x2 - x1) * rr2 + rr1) + root) / (2 * rr2)
        delta2 = (-((x2 - x1) * rr2 + rr1) - root) / (2 * rr2)
        delta0 = delta1 if abs(delta1) < abs(delta2) else delta2
        x3 = x2 + delta0
        
        if abs(x3 - x2) <= eps or abs(f(x3)) <= eps:
            print(f"Solution = {x3}\nWith iteration {k + 1}")
            return x3, k + 1

    print("Solution not found")
    return None, kmax

# Main execution
if __name__ == "__main__":
    eps = 1e-10
    kmax = 10000
    x0 = 5.0
    
    methods = [
        Simple_Iteration,
        Method_Newton,
        Method_Chebysheva,
        Method_Hord,
        Method_Parabol
    ]
    
    for method in methods:
        solution, iterations = method(kmax, eps, x0)
        if solution:
            print(f"\n{method.__name__} found solution {solution} in {iterations} iterations.")
