# Enter two distinct faces as vectors u and v.

import numpy as np
from PIL import Image

a = Image.open("shriram.jpg.webp")
b = Image.open("Shiva.jpeg")
a.show()
b.show()
i1 = np.asarray(a)
i2 = np.asarray(b)
print("co-ordinates of img1", i1)
print("co-ordinates of img2", i2)
