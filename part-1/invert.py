import cv2

img = cv2.imread('source/2.jpg')
res = cv2.bitwise_not(img)
cv2.imshow('original', img)
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()