from math import gcd
from sympy import symbols, diff, Matrix, sympify


#linear congruence start
def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # No solution
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def solve_linear_congruence(a, b, m):
    """
    Solves ax ≡ b mod m and returns all solutions or None if no solution exists.
    """
    a, b, m = int(a), int(b), int(m)
    g = gcd(a, m)

    if b % g != 0:
        return None  

    # Simplify equation
    a1 = a // g
    b1 = b // g
    m1 = m // g

    inv = modinv(a1, m1)
    if inv is None:
        return None

    x0 = (inv * b1) % m1
    # Generate all solutions
    solutions = [(x0 + i * m1) % m for i in range(g)]
    return solutions
#liner congruence end



#stokes theorem start
def stokes_theorem_curl(fx, fy, fz):
    x, y, z = symbols('x y z')
    Fx = sympify(fx)
    Fy = sympify(fy)
    Fz = sympify(fz)

    # curl(F) = [∂Fz/∂y - ∂Fy/∂z, ∂Fx/∂z - ∂Fz/∂x, ∂Fy/∂x - ∂Fx/∂y]
    curl_x = diff(Fz, y) - diff(Fy, z)
    curl_y = diff(Fx, z) - diff(Fz, x)
    curl_z = diff(Fy, x) - diff(Fx, y)

    return Matrix([curl_x, curl_y, curl_z])
#stokes theorem end