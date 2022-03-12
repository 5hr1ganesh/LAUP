# Create a new Plot by rotating the given number by 180degrees

import matplotlib.pyplot as plt

x = 2 + 4j
plt.scatter(x.real, x.imag, color='red')
plt.scatter(-1 * x.real, -1 * x.imag, color='blue')
plt.show()
