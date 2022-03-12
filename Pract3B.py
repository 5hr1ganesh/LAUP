import numpy as np
from PIL import Image

a = Image.open("Shiva_copy.jpeg")
b = Image.open("Shiva.jpeg")
# a.show()
# b.show()
i1 = np.asarray(a)
i2 = np.asarray(b)
# print(i1)
# print(i2)
x = 1
y = 2
lc = x * i1 + y * i2
lm = Image.fromarray(lc)
lm.show()
