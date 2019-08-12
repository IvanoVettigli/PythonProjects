import matplotlib.pyplot as mpl
import math
import numpy

k = 0.01
l = k
t = [0]

xi = [1]
vi = [0]
E = [0.5*(pow(vi[0], 2)+pow(2*math.pi*xi[0], 2))]

xiE = [1]
viE = [0]
EE = [0.5*(pow(viE[0], 2)+pow(2*math.pi*xiE[0], 2))]

xiEC = [1]
viEC = [0]
EEC = [0.5*(pow(viEC[0], 2)+pow(2*math.pi*xiEC[0], 2))]

xiKV = [1]
viKV = [0]
EKV = [0.5*(pow(viKV[0], 2)+pow(2*math.pi*xiKV[0], 2))]


for i in range(1, 401):

    t.append(k)

    xi.append(math.cos(2*math.pi*t[i]))
    vi.append(-2*math.pi*math.sin(2*math.pi*t[i]))
    E.append(0.5*(pow(vi[i], 2)+pow(2*math.pi*xi[i], 2)))

    k += l

    xiE.append(xiE[i-1]-viE[i-1]*l)
    viE.append(viE[i-1]+pow(2*math.pi, 2)*xiE[i-1]*l)
    EE.append(0.5*(pow(viE[i], 2)+pow(2*math.pi*xiE[i], 2)))

    viEC.append(viEC[i-1]-pow(2*math.pi, 2)*xiEC[i-1]*l)
    xiEC.append(xiEC[i-1]+viEC[i-1]*l-pow(2*math.pi, 2)*xiEC[i-1]*pow(l, 2))
    EEC.append(0.5*(pow(viEC[i], 2)+pow(2*math.pi*xiEC[i], 2)))

    xiKV.append(xiKV[i-1]+viKV[i-1]*l-2*pow(l*math.pi, 2)*xiKV[i-1])
    viKV.append(viKV[i-1]-2*l*pow(math.pi, 2)*(xiKV[i-1]+xiKV[i]))
    EKV.append(0.5*(pow(viKV[i], 2)+pow(2*math.pi*xiKV[i], 2)))


print(numpy.mean(E), "\n", numpy.abs(numpy.mean(E)-numpy.mean(EE)),
      "\n", numpy.abs(numpy.mean(E)-numpy.mean(EEC)), "\n",
      numpy.abs(numpy.mean(E)-numpy.mean(EKV)))

mpl.figure()
mpl.plot(t, xi, t, xiE, t, xiEC, t, xiKV)
mpl.title('Position in time')
mpl.xlabel('time [s]')
mpl.ylabel('position [m]')
mpl.legend("EACK")
mpl.grid()

mpl.figure()
mpl.plot(t, vi, t, viE, t, viEC, t, viKV)
mpl.title('velocity in time')
mpl.xlabel('time [s]')
mpl.ylabel('velocity [m/s]')
mpl.legend("EACK")
mpl.grid()

mpl.figure()
mpl.plot(t, E, t, EE, t, EEC, t, EKV)
mpl.title('Energy')
mpl.xlabel('time [s]')
mpl.ylabel('Energy [J]')
mpl.legend('EACK')

mpl.show()


xiKVR = [xiKV[len(xiKV)-1]]
viKVR = [viKV[len(viKV)-1]]

for i in range(401):

    xiKVR.append(xiKV[i-1]+viKV[i-1]*l-2*pow(l*math.pi, 2)*xiKV[i-1])
    viKVR.append(viKV[i-1]-2*l*pow(math.pi, 2)*(xiKV[i-1]+xiKV[i]))
    EKV.append(0.5*(pow(viKV[i], 2)+pow(2*math.pi*xiKV[i], 2)))
