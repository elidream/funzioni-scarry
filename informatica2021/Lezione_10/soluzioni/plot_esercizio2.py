import numpy as np
import matplotlib.pyplot as plt

# load data
data = np.loadtxt("../data2.dat")

# plot points
plt.errorbar(data[:,0], data[:,1], yerr=0.1, fmt='.', label='data')

# cosmetics
plt.title("Esercizio 2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# save file to disk
plt.savefig("esercizio2.png")

# show plot
plt.show()
