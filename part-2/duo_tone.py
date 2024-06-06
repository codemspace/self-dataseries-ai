import cv2
import numpy as np


def exponential_function(channel, exp):
    table = np.array([min((i ** exp), 255) for i in np.arange(0, 256)]).astype("uint8")  # creating table for exponent
    channel = cv2.LUT(channel, table)
    return channel


def tone(img, number):
    for i in range(3):
        if i == number:
            img[:, :, i] = exponential_function(img[:, :, i], 1.05)  # applying exponential function on slice
        else:
            img[:, :, i] = 0  # setting values of all other slices to 0
    return img


img = cv2.imread('../source/2.jpg')
original = img.copy()
img = tone(img, 1)  # change second parameter to 0 for blue, 1 for green and 2 for red screen
cv2.imshow('original', original)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
