import cv2
import numpy as np


def gamma_function(channel, gamma):
    invGamma = 1 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")  # creating lookup table
    channel = cv2.LUT(channel, table)
    return channel


img = cv2.imread('source/2.jpg')
original = img.copy()
img[:, :, 0] = gamma_function(img[:, :, 0], 0.75)  # down scaling blue channel
img[:, :, 2] = gamma_function(img[:, :, 2], 1.25)  # up scaling red channel
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:, :, 1] = gamma_function(hsv[:, :, 1], 1.2)  # up scaling saturation channel
img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('Original', original)
cv2.imshow('Summer', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
