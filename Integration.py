import numpy
import math

import matplotlib.pyplot as mpl


def romberg(f, a, b, n):
    """Estimate the integral of f(x) from a to b using Romberg Integration.

    USAGE:
        r = romberg( f, a, b, n )

    INPUT:
        f       - function to integrate,
        [a, b]  - the interval of integration,
        n       - number of levels of recursion

    OUTPUT:
        numpy float array - Romberg integration array; most accurate
                            answer should be at bottom of right-most column,

    NOTES:
        Based on an algorithm in "Numerical Mathematics and Computing"
        4th Edition, by Cheney and Kincaid, Brooks-Cole, 1999.

    AUTHOR:
        Jonathan R. Senning <jonathan.senning@gordon.edu>
        Gordon College
        February 17, 1999
        Converted to Python August 2008
    """

    r = numpy.array([[0] * (n + 1)] * (n + 1), float)
    h = b - a
    r[0, 0] = 0.5 * h * (f(a) + f(b))

    powerOf2 = 1
    for i in range(1, n + 1):

        # Compute the halved stepsize and use this to sum the function at
        # all the new points (in between the points already computed)

        h = 0.5 * h

        sum = 0.0
        powerOf2 = 2 * powerOf2
        for k in range(1, powerOf2, 2):
            sum = sum + f(a + k * h)

        # Compute the composite trapezoid rule for the next level of
        # subdivision.  Use Richardson extrapolation to refine these values
        # into a more accurate form.

        r[i, 0] = 0.5 * r[i - 1, 0] + sum * h

        powerOf4 = 1
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            r[i, j] = r[i, j - 1] + (r[i, j - 1] - r[i - 1, j - 1]) / (powerOf4 - 1)
            print(r[i,j])
    return r


# function we want to integrate
def f(x):
    # noinspection PyUnresolvedReferences
    return math.exp(x)

# noinspection PyUnresolvedReferences
# call quad to integrate f from -2 to 2
z = romberg(f, 0, 1, 4)



