import imageio.v3 as iio
import numpy as np
from PIL import Image


image_files = ["png1.png", "png2.png", "png3.png"]


images = []

for file_name in image_files:
    img = Image.open(file_name)
    img_rgb = img.convert("RGB")
    img_array = np.array(img_rgb)
    images.append(img_array)


iio.imwrite("output.gif", images, duration=0.5,loop=0)
