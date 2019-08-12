import matplotlib.pyplot as mpl
import math
import numpy

h = 0.0001
L = h
t = [0]

g = 9.81
l = 1
m = 1

theta = [0.5 * math.pi]
p = [0]

F = [- m * g * l * math.sin(theta[0])]

x = [l * math.sin(theta[0])]

E = [0.5 * pow(p[0], 2) / m + m * g * l * (1 - math.cos(theta[0]))]


for i in range(1, 80001):

    theta.append(theta[i-1]+p[i-1]*h+0.5*F[i-1]*pow(h, 2))

    F.append(- m * g * l * math.sin(theta[i]))

    p.append(p[i-1]+0.5*(F[i-1]+F[i])*h)

    x.append(l * math.sin(theta[i]))

    E.append(0.5 * pow(p[i], 2) / m + m * g * l * (1 - math.cos(theta[i])))

    t.append(L)
    L += h


print(E[0], "\n", E[0]-numpy.mean(E))

mpl.figure()
mpl.plot(t, theta)
mpl.grid()

mpl.figure()
mpl.plot(t, x)
mpl.grid()

mpl.figure()
mpl.plot(t, p)

mpl.figure()
mpl.plot(t, E)
mpl.grid()

mpl.show()
