

import numpy as np
from skimage import io
import matplotlib.pyplot as plt


camaro = io.imread("camaro.jpg")
print(camaro)


camaro.shape


plt.imshow(camaro)
plt.show()


# Cropping the image


cropped = camaro[0:500,:,:]
plt.imshow(cropped)
plt.show()


cropped = camaro[:,400:1000,:]
plt.imshow(cropped)
plt.show()


cropped = camaro[350:1000,200:1400,:]
plt.imshow(cropped)
plt.show()


io.imsave("camaro_cropped.jpg", cropped)