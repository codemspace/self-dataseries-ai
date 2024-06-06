import cv2

img = cv2.imread('../source/2.jpg')
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07,
                                       shade_factor=0.05)  # inbuilt function to generate pencil sketch in both color and grayscale
# sigma_s controls the size of the neighborhood. Range 1 - 200
# sigma_r controls the how dissimilar colors within the neighborhood will be averaged. A larger sigma_r results in large regions of constant color. Range 0 - 1
# shade_factor is a simple scaling of the output image intensity. The higher the value, the brighter is the result. Range 0 - 0.1
cv2.imshow("Image", img)
cv2.imshow("Output2", dst_gray)
cv2.imshow("Output", dst_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
