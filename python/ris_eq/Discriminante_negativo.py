import cmath

def discriminante_negativo(a, b, delta):

    """Risolve equazioni di secondo grado con determinante negativo"""

    ix1 = (-b - cmath.sqrt(delta))/(2*a)
    ix2 = (-b + cmath.sqrt(delta))/(2*a)

    print(" \n Le soluzioni immaginarie sono", "\n x1 = " \
    , ix1, "\n x2 = ", ix2)
