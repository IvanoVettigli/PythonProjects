import matplotlib.pyplot as mpl


t = []
for i in range(51):
    t.append(i)


xi = [1]
vi = [0]

print(xi[0], vi[0])

for i in range(50):
    xi.append(xi[i-1]+vi[i-1])
    vi.append(vi[i-1]-xi[i-1])


mpl.plot(t, xi)
mpl.grid()
mpl.show()
