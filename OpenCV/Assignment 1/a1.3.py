import cv2 as cv
import sys

original = cv.imread("rhythm_of_colors.jpg")

if original is None:
	sys.exit("Could not find image")

#Converting image from BGR (default) to RGB
converted = cv.cvtColor(original, cv.COLOR_BGR2RGB)

cv.imshow('Original BGR', original)
cv.imshow('Converted RGB', converted)

k = cv.waitKey(0)
if k == ord('s'):
	cv.imwrite("bgr_to_rgb.jpg", converted)

#cv.destroyAllWindows()