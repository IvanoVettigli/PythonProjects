import matplotlib.pyplot as mpl
import math
import numpy

L = 0.01
h = L
t = [0]

xi = [1]
vi = [0]
E = [0.5*(pow(vi[0], 2)+pow(2*math.pi*xi[0], 2))]

xiRK = [1]
viRK = [0]
ERK = [0.5*(pow(viRK[0], 2)+pow(2*math.pi*xiRK[0], 2))]


for i in range(1, 401):

    xi.append(math.cos(2*math.pi*t[i-1]))
    vi.append(-2*math.pi*math.sin(2*math.pi*t[i-1]))
    E.append(0.5*(pow(vi[i], 2)+pow(2*math.pi*xi[i], 2)))

    k1x = viRK[i-1]
    k1v = -pow(2*math.pi, 2)*xiRK[i-1]

    k2x = viRK[i-1]+h*0.5*k1v
    k2v = -pow(2*math.pi, 2)*xiRK[i-1]-h*0.5*k1x

    k3x = viRK[i-1]+h*0.5*k2v
    k3v = -pow(2*math.pi, 2)*xiRK[i-1]-h*0.5*k2x

    k4x = viRK[i-1]+h*0.5*k3v
    k4v = -pow(2*math.pi, 2)*xiRK[i-1]-h*0.5*k3x

    xiRK.append(xiRK[i-1]+h/6*(k1x+2*k2x+2*k3x+k4x))
    viRK.append(viRK[i-1]+h/6*(k1v+2*k2v+2*k3v+k4v))

    ERK.append(0.5*(pow(viRK[i], 2)+pow(2*math.pi*xiRK[i], 2)))

    t.append(L)
    L += h


print(numpy.mean(E), "\n", numpy.abs(numpy.mean(E)-numpy.mean(ERK)))

mpl.figure()
mpl.plot(t, xi, t, xiRK)
mpl.title('Position in time')
mpl.xlabel('time [s]')
mpl.ylabel('position [m]')
mpl.legend("EA")
mpl.grid()

mpl.figure()
mpl.plot(t, vi, t, viRK)
mpl.title('velocity in time')
mpl.xlabel('time [s]')
mpl.ylabel('velocity [m/s]')
mpl.legend("EA")
mpl.grid()

mpl.figure()
mpl.plot(t, E, t, ERK)
mpl.title('Energy')
mpl.xlabel('time [s]')
mpl.ylabel('Energy [J]')
mpl.legend('EA')

mpl.show()
