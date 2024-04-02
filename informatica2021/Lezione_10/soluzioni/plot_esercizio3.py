import numpy as np
import matplotlib.pyplot as plt

# load data
data = np.loadtxt("../data3.dat")

# plot points
plt.hist(data, bins=50, range=(-20, 25), label="data")

# cosmetics
plt.title("Esercizio 3")
plt.xlabel("x")
plt.ylabel("Frequenza")
plt.legend()

# save file to disk
plt.savefig("esercizio3.png")

# show plot
plt.show()
