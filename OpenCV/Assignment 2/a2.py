import cv2 as cv
import numpy as np 
import sys

img = cv.imread("task2_img.png", 0)
rows,cols = img.shape

transform = []

if img is None:
	sys.exit("Could not read the image.")

#Scaling / resizing
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

#Translating
for i in range(1,5):
	M = np.float32([[1,0,40*i],[0,1,50]]) 
	transform.append(cv.warpAffine(img,M,(cols,rows)))

#Rotating
for i in range(5,9):
	M = cv.getRotationMatrix2D((cols/2,rows/2),18*i,1)
	transform.append(cv.warpAffine(img,M,(cols,rows)))
	

#Blur
transform.append(cv.blur(img,(5,5)))

transform.append(cv.GaussianBlur(img,(5,5),0))

for i in transform:
	cv.imshow("Transformed", i)
	cv.waitKey(0)
	cv.destroyAllWindows()