# Create a new Plot by rotating the given number by 270degrees

import matplotlib.pyplot as plt

x = 2 + 4j
z = -1j
plt.scatter(x.real, x.imag, color='red')
c = x * z
plt.scatter(c.real, c.imag)
plt.show()
