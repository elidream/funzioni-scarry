# import libraries
import numpy as np
import matplotlib.pyplot as plt

# load data
data = np.loadtxt("../data5.dat")

# plot
plt.plot(data[:,0], data[:, 1], 'o', label='(x,y)')
plt.plot(data[:,0], data[:, 2], 'o', label='(x,z)')

plt.title("Campionamento funzioni da file")
plt.xlabel("x")
plt.legend()

# save file to disk
plt.savefig("output5.png")

# open canvas
plt.show()
