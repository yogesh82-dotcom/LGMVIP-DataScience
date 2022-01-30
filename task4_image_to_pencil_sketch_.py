# -*- coding: utf-8 -*-
"""Task4 Image-to-Pencil Sketch .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sEdJs-fw04i2xpSwziGzh9OVbpK-X7eW
"""



"""# New Section"""

from google.colab.patches import cv2_imshow

import cv2

img = cv2.imread("dhoni.png")

cv2_imshow(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2_imshow(img_gray)

img_invert = cv2.bitwise_not(img_gray)

cv2_imshow(img_invert)

img_smoothing = cv2.GaussianBlur(img, (21, 21), sigmaX=0, sigmaY=0)
img_smoothing_gray = cv2.GaussianBlur(img_gray, (21, 21), sigmaX=0, sigmaY=0)
img_smoothing_gray_invert = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
cv2_imshow(img_smoothing)
cv2_imshow(img_smoothing_gray)
cv2_imshow(img_smoothing_gray_invert)

inverted_blurred = 255 - img_smoothing_gray_invert
pencil_sketch = cv2.divide(img_gray, inverted_blurred, scale=256.0)
cv2_imshow(img)
cv2_imshow(pencil_sketch)