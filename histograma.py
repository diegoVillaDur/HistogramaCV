import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv.imread("Aquelarre.jpg")

b = img_bgr[:, :, 0]
g = img_bgr[:, :, 1]
r = img_bgr[:, :, 2]

hist_b = np.zeros(256, dtype=int)
hist_g = np.zeros(256, dtype=int)
hist_r = np.zeros(256, dtype=int)

for pixel in b.ravel():
    hist_b[pixel] += 1

for pixel in g.ravel():
    hist_g[pixel] += 1

for pixel in r.ravel():
    hist_r[pixel] += 1

img_rgb = np.dstack([r, g, b])

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Imagen")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.plot(hist_r, color="red", label="Rojo", alpha=0.8)
plt.plot(hist_g, color="green", label="Verde", alpha=0.8)
plt.plot(hist_b, color="blue", label="Azul", alpha=0.8)

plt.title("Histograma")
plt.xlabel("Valor pixel")
plt.ylabel("Frec")
plt.xlim([0, 255])
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
