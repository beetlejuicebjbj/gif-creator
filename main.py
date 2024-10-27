import imageio.v3 as iio  # imageio v3 sürümünü kullanıyorsanız
import numpy as np
from PIL import Image

# Görüntü dosyalarını yükle
image_files = ["png1.png", "png2.png", "png3.png"]  # Bu kısma görüntü dosya adlarınızı ekleyin

# Görüntüleri bir listeye yükleyin
images = []

for file_name in image_files:
    img = Image.open(file_name)   # Görüntüyü aç
    img_rgb = img.convert("RGB")  # RGB formatına dönüştür
    img_array = np.array(img_rgb)  # NumPy dizisine dönüştür
    images.append(img_array)  # Listeye ekle

# GIF oluştur
iio.imwrite("output.gif", images, duration=0.5,loop=0)  # duration parametresi her kare arasındaki gecikmeyi belirler
