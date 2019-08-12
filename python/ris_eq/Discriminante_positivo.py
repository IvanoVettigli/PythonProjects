import math

def discriminante_positivo(a, b, delta):

    """Risolve equazioni di secondo grado con discriminante positivo"""

    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print("\nIl discriminante è positivo, ho trovato due soluzioni \n x1= ", x1, " \n x2= ", x2)
