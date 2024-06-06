import cv2
import numpy as np

img = cv2.imread('source/2.jpg')
original = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
xp = [0, 64, 112, 128, 144, 192, 255]  # setting reference values
fp = [0, 16, 64, 128, 192, 240, 255]  # setting values to be taken for reference values
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')  # creating lookup table
img = cv2.LUT(gray, table)  # changing values based on lookup table
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
