import pylab as lab
import math

hbar = 6.626 * 10**(-34)
m = 10**(-30)
w = 1
pi = 3.14159


def psi(x):
    return ((m * w)/(pi * hbar))**(1/4) * math.exp(- (m * w) / (2 * hbar) * x**2)


def psi_2(x):
    return ((m * w)/(pi * hbar))**(1/4) * math.sqrt((2 * m * w)/(hbar)) * x * math.exp(- (m * w) / (2 * hbar) * x**2)

x_out = []
psi_out = []
psi_2_out = []
p_psi_out = []
p_psi_2_out = []

for x in range(-150, 150):
    x_out.append(x/1000)
    psi_out.append(psi(x/1000))
    psi_2_out.append(psi_2(x/1000))
    p_psi_out.append(psi(x/1000)**(2))
    p_psi_2_out.append(psi_2(x/1000)**(2))

# Plot
lab.plot(x_out, psi_out, "-b", label="n = 0")
lab.plot(x_out, psi_2_out, "-g", label="n = 1")
lab.plot(x_out, p_psi_out, "--b", label="$P[\psi_0]$")
lab.plot(x_out, p_psi_2_out, "--g", label="$P[\psi_1]$")
lab.xlabel("x")
lab.ylabel("$\psi$")
lab.legend(loc='upper right')
lab.show()
