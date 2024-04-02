# import libraries
import numpy as np
import matplotlib.pyplot as plt

# load data
data = np.loadtxt("../data1.dat")

# plot
plt.plot(data[:,0], data[:, 1], 'or')
plt.title("Distribuzione di particelle cariche")
plt.xlabel("Coordinata x")
plt.ylabel("Coordinata y")

# save file to disk
plt.savefig("output.png")

# open canvas
plt.show()
