import cv2 as cv 
import sys

img = cv.imread(cv.samples.findFile("rhythm_of_colors.jpg"))

# Step 1 - obtain grayscale image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Step 2 - obtain inverse of grayscale OR negative of image
img_gray_inv = 255 - img_gray

# Step 3 - gaussian blur
img_blur = cv.GaussianBlur(img_gray_inv, ksize=(21,21), sigmaX=0, sigmaY=0)

# Step 4 - blend
#pencil_sketch = cv.Laplacian(img, cv.CV_64F)

def dodgeV2(image, mask):
	return cv.divide(image, 255-mask, scale=256)

def burnV2(image, mask):
	return 255 - cv.divide(255-image, 255-mask, scale=256)

pencil_sketch = dodgeV2(img_gray, img_blur)

cv.imshow("Original", img)
cv.imshow("GrayScale", img_gray)
cv.imshow("Negative", img_gray_inv)
cv.imshow("Blurred Negative", img_blur)
cv.imshow("Pencil Sketch", pencil_sketch)


k = cv.waitKey(0)
if k == ord('s'):
	cv.imwrite("Pencil Sketch", pencil_sketch)

#cv.destroyAllWindows()