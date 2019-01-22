import cv2 as cv

image = cv.imread('images/test.jpg', cv.IMREAD_GRAYSCALE)

image_sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
image_sobel_x = cv.convertScaleAbs(image_sobel_x)

image_sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)
image_sobel_y = cv.convertScaleAbs(image_sobel_y)

image_sobel = cv.addWeighted(image_sobel_x, 1, image_sobel_y, 1, 0)

cv.imshow("sobel x", image_sobel_x)
cv.imshow("sobel y", image_sobel_y)
cv.imshow("sobel", image_sobel)

cv.waitKey(0)
cv.destoryAllWindows()