import os
import sys
from pathlib import Path

import cv2

base_dir = Path(__file__).resolve().parent
img1_path = base_dir / "Aquelarre.jpg"
img2_path = base_dir / "ParejasReales.jpg"

img1 = cv2.imread(str(img1_path), cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(str(img2_path), cv2.IMREAD_GRAYSCALE)

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

dest_and = cv2.bitwise_and(img1, img2)
dest_or = cv2.bitwise_or(img1, img2)
dest_xor = cv2.bitwise_xor(img1, img2)
dest_not = cv2.bitwise_not(img1)

results = {
    "Original 1": img1,
    "Original 2": img2,
    "Bitwise AND": dest_and,
    "Bitwise OR": dest_or,
    "Bitwise XOR": dest_xor,
    "Bitwise NOT": dest_not,
}

output_dir = base_dir / "resultados_operadores"
output_dir.mkdir(exist_ok=True)

show_images = os.environ.get("SHOW_IMAGES", "0").lower() in {"1", "true", "yes"}

if show_images:
    try:
        for title, image in results.items():
            cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error:
        show_images = False

if not show_images:
    for title, image in results.items():
        filename = title.replace(" ", "_").lower() + ".png"
        cv2.imwrite(str(output_dir / filename), image)
    print(f"Se guardaron las imágenes en: {output_dir}")
