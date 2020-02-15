import numpy as np
import matplotlib.pyplot as plt

# constants
mass = 1
m0=1
hbar=1
scaling = 50

# harmonic potential
xstart = -5
xend = 5
N=100

x=np.linspace(xstart, xend, N)
potential = 1/2*x**2   # harmonic oscilator
#potential = -abs(10/x)  # coulomb (atom)
plt.plot(x, potential)

# assemble H matrix and diagonalize
dx= (xend-xstart)/N
t0 = hbar**2/(2*mass*dx**2)
H = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        if i == j:
            H[i][j] = potential[i] + 2*t0
        if i == (j+1):
            H[i][j] = -t0
        if i == (j-1):
            H[i][j] = -t0
energy,wavefunctions = np.linalg.eigh(H)

for i in range(5):
    plt.plot(x,wavefunctions[:,i]**2*scaling + energy[i])
print(energy[:5])

