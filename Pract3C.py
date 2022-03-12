# Find the average face of the original faces

from PIL import Image
import numpy as np

a = Image.open("Shiva_copy.jpeg")
b = Image.open("Shiva.jpeg")
i1 = np.asarray(a)
i2 = np.asarray(b)
i = i1 + i2
agm = i / 2
ag = Image.fromarray(np.uint8(agm), None)
# mode: Literal["1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"] | None = ...)
#   -> Image
ag.show()
