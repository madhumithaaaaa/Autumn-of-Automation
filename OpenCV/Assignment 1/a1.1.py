import cv2 as cv
import sys

# 1.1

img = cv.imread(cv.samples.findFile("rhythm_of_colors.jpg"))

if img is None:
	sys.exit("Could not read the image.")

#cv.imshow("Display window", img)
#k = cv.waitKey(0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
cv.imshow('Original image',img)
cv.imshow('Gray image', gray)
  
k = cv.waitKey(0)
if k == ord("s"):
	cv.imwrite("rhythm_of_colors.jpg", img)
	cv.imwrite("grayscale.jpg", gray)


