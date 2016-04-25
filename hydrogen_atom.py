import pylab as lab
import numpy as np

r = np.linspace(0, 7, 200)

psi_10 = 1 / np.sqrt(np.pi) * np.exp(-r)
psi_20 = 1/(4 * np.sqrt(2 * np.pi)) * (2 - r) * np.exp(-r)

p_psi_10 = psi_10 * psi_10 * r * r
p_psi_20 = psi_20 * psi_20 * r * r

# Plot
# lab.plot(r, psi_10, "-r", label="$\psi_1$")
# lab.plot(r, psi_20, "-g", label="$\psi_2$")
# lab.plot(r, p_psi_10, "-r", label="$P[\psi_1]$")
lab.plot(r, p_psi_20, "-g", label="$P[\psi_1]$")
lab.xlabel("x")
lab.ylabel("$\psi$")
lab.legend(loc='upper right')
lab.show()
