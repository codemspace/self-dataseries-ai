import cv2
import numpy as np

img = cv2.imread('source/2.jpg')
image_HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)  # Conversion to HLS
image_HLS = np.array(image_HLS, dtype=np.float64)
daylight = 1.15
image_HLS[:, :, 1] = image_HLS[:, :, 1] * daylight  # scale pixel values up for channel 1(Lightness)
image_HLS[:, :, 1][image_HLS[:, :, 1] > 255] = 255  # Sets all values above 255 to 255
image_HLS = np.array(image_HLS, dtype=np.uint8)
image_RGB = cv2.cvtColor(image_HLS, cv2.COLOR_HLS2BGR)  # Conversion to RGB
cv2.imshow("original", img)
cv2.imshow("Output", image_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
