import cv2
import numpy as np

img = cv2.imread('source/2.jpg')
height, width = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = 0.8  # creating threshold. This means noise will be added to 80% pixels
for i in range(height):
    for j in range(width):
        if np.random.rand() <= thresh:
            if np.random.randint(2) == 0:
                gray[i, j] = min(gray[i, j] + np.random.randint(0, 64),
                                 255)  # adding random value between 0 to 64. Anything above 255 is set to 255.
            else:
                gray[i, j] = max(gray[i, j] - np.random.randint(0, 64),
                                 0)  # subtracting random values between 0 to 64. Anything below 0 is set to 0.
cv2.imshow("original", img)
cv2.imshow("Output", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
