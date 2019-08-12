import numpy
import matplotlib.pyplot as mpl

L = 10
N = L*L
STEPS = 1000


def build_lattice(L):

    lattice = numpy.zeros((L, L))

    for i in range(L): 

        for j in range(L):
        
            lattice[i, j] = 1
            
    return lattice

    
def bc(i):

    if i+1 > L-1:
        return 0
    if i-1 < 0:
        return L-1
    else:
        return i       
    

def delta_energy(lattice, i, j):

    return lattice[i, j] * (lattice[bc(i-1), j] +
                             lattice[bc(i+1), j] +
                             lattice[i, bc(j-1)] +
                             lattice[i, bc(j+1)])

    

def magnetization(T):
    
    M = [L*L]

    lattice = build_lattice(L)

    for n in range(STEPS):

        for k in range(N):

            i = numpy.random.randint(0, L)
            j = numpy.random.randint(0, L)
            DE = delta_energy(lattice, i, j)
        
            if DE < 0:
            
                lattice[i, j] = -lattice[i, j]
            
            elif numpy.exp(-1/T*DE) > numpy.random.rand(1, 1):
            
                lattice[i, j] = -lattice[i, j]
            
        if n % 100 == 0:
        
            M.append(lattice.sum())

    print(numpy.mean(M), numpy.std(M))

    mpl.figure()
    mpl.plot(M)
    mpl.grid()
    mpl.show()
    
    return numpy.mean(M)

#magnetization(2.3)

def critical_temperature():
    M_T=[]
    T=.1    

    for t in range(1000):
        M_T.append(magnetization(T))    
        T = T+t/2000
        
    mpl.figure()
    mpl.plot(M_T)
    mpl.title()
    mpl.grid()
    mpl.show()
    
#critical_temperature() 