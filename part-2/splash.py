import cv2
import numpy as np


def hsv(img, l, u):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([l, 128, 128])  # setting lower HSV value
    upper = np.array([u, 255, 255])  # setting upper HSV value
    mask = cv2.inRange(hsv, lower, upper)  # generating mask
    return mask


img = cv2.imread('../source/colors.jpg')
original = img.copy()
res = np.zeros(img.shape, np.uint8)  # creating blank mask for result
l = 15  # the lower range of Hue we want
u = 30  # the upper range of Hue we want
mask = hsv(img, l, u)
inv_mask = cv2.bitwise_not(mask)  # inverting mask
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res1 = cv2.bitwise_and(img, img, mask=mask)  # region which has to be in color
res2 = cv2.bitwise_and(gray, gray, mask=inv_mask)  # region which has to be in grayscale
for i in range(3):
    res[:, :, i] = res2  # storing grayscale mask to all three slices
img = cv2.bitwise_or(res1, res)  # joining grayscale and color region
cv2.imshow('original', original)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
