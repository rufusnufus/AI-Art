import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from math import ceil

image = cv2.imread("./img/panda.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image.shape
GRID_SIZE = 10

height_offset = ceil(height / GRID_SIZE) * GRID_SIZE - height
width_offset = ceil(width / GRID_SIZE) * GRID_SIZE - width
image = cv2.copyMakeBorder(image, 0, height_offset, 0, width_offset, cv2.BORDER_REFLECT)
height, width, _ = image.shape

print(height, width)
plt.imshow(image)
plt.show()