# Define f(x) and g(x)
def f(x):
    return x


def g(x):
    return 17 * x + 1


# Choose x0 as any positive number, let's say 1
x0 = 1


# Define a function to find C1 and C2
def find_constants(x0):
    # Evaluate f(x0) and g(x0)
    fx0 = f(x0)
    gx0 = g(x0)

    # Initialize C1 and C2
    C1 = 1 / abs(gx0)
    C2 = abs(fx0) - C1 * abs(gx0)

    return C1, C2


# Find constants C1 and C2 for given x0
C1, C2 = find_constants(x0)

print("x0:", x0)
print("Constants C1 and C2:")
print("C1:", C1)
print("C2:", C2)
