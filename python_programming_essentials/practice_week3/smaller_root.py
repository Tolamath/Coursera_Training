"""
This program solves the quadratic equation
"""
def smaller_root(coeff_a, coeff_b, coeff_c):
    """
    This function takes in three inputs coeff_a, coeff_b and coeff_c and computes the
    discriminant, once it's greater than or equal to zero. Otherwise
    returns "Error: No real solutions"
    """
    determinant = (coeff_b**2 - (4*coeff_a*coeff_c))
    if determinant  > 0:
        return (-coeff_b + determinant**0.5)/(2*coeff_a), (-coeff_b - determinant**0.5)/(2*coeff_a)
    if determinant == 0:
        return -coeff_b/(2*coeff_a)
    return "Error: No real solutions"
print("Enter the values of coeff_a, coeff_b and coeff_c: ")
a_coeff, b_coeff, c_coeff = map(int, input().split())
print("The solutions are:")
print(smaller_root(a_coeff,b_coeff,c_coeff))
