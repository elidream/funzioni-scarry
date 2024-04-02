import numpy as np
import matplotlib.pyplot as plt

# load data
data_dentro = np.loadtxt("dentro.dat")
data_fuori = np.loadtxt("fuori.dat")

# plot points
plt.plot(data_dentro[:,0], data_dentro[:,1], "ob", label="dentro")
plt.plot(data_fuori[:,0], data_fuori[:,1], "or", label="fuori")

# cosmetics
plt.title("Esercizio 1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# save file to disk
plt.savefig("esercizio1.png")

# show plot
plt.show()
