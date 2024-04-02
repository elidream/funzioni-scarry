# import libraries
import numpy as np
import matplotlib.pyplot as plt

# load data
data = np.loadtxt("output.dat")

# plot
plt.plot(data[:,0], data[:, 1], 'o-', label='$-\\frac{sin(x^2)}{x} + 0.01 * x^2$')
plt.title("Campionamento funzione da file")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim([-3,3])
plt.legend(frameon=False)

# save file to disk
plt.savefig("output4.png")

# open canvas
plt.show()
