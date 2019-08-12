import math
import matplotlib.pyplot as mpl
import cmath

xi = []
yi = []

print("Ciao! io sono un simpatico programma e risolverò per te un'equazione,\
 ma a patto che sia nella forma ax^2+bx+c=0")

a = float(input(" Quanto vale a? "))
b = float(input(" E b? "))
c = float(input(" last but not least, c? "))

delta = b**2-4*a*c


if delta < 0:
    print("\n Mi dispiace ma il determinante è negativo, non ho trovato soluzioni reali!\
    A breve il mio creatore mi insegnerà a trovare le soluzioni complesse! o almeno spero...")
    ix1 = (-b - cmath.sqrt(delta))/(2*a)
    ix2 = (-b + cmath.sqrt(delta))/(2*a)

    print("Le soluzioni immaginarie sono", "\n", ix1, "\n ", ix2)


elif delta == 0:
    x = -b/(2*a)
    print("\n Il discriminante è nullo, ho trovato due soluzioni coincidenti! \n x= ", x)
    valore = input(" \n Vuoi il grafico della parabola? ")
    if "Si" == valore:
        j = 0
        for j in range(10, 0, -1):
            xi.append(x-j)
            yi.append(a*xi[10-j]**2+b*xi[10-j]+c)
        xi.append(x)
        yi.append(a*xi[10]**2+b*xi[10]+c)
        for j in range(0, 11, 1):
            xi.append(x+j)
            yi.append(a*xi[11+j]**2+b*xi[11+j]+c)
        mpl.plot(xi, yi)
        mpl.show()
else:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print("\nIl discriminante è positivo, ho trovato due soluzioni \n x1= ", x1, " \n x2= ", x2)
    valore = input(" \n Vuoi il grafico della parabola? ")
    if "Si" == valore:
        j = 0
        for j in range(10, 0, -1):
            xi.append(x1-j)
            yi.append(a*xi[10-j]**2+b*xi[10-j]+c)
        xi.append(x1)
        yi.append(a*xi[10]**2+b*xi[10]+c)
        for j in range(0, 11, 1):
            xi.append(x1+j)
            yi.append(a*xi[11+j]**2+b*xi[11+j]+c)
        mpl.plot(xi, yi)
        mpl.show()
