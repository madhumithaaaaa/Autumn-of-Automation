import cv2 as cv
import numpy as np 
import imutils


def detect(c):
	shape = "unidentified"
	perimeter = cv.arcLength(c, True)
	approx = cv.approxPolyDP(c, 0.04*perimeter, True)

	#Triangle - 3
	if len(approx) == 3:
		shape = "triangle"

	#Square / Rectangle - 4
	elif len(approx) == 4:
		#compute aspect ratio
		(x,y,w,h) = cv.boundingRect(approx)
		if cv.contourArea(c) == w*h:

			if w==h:
				shape = "square"
			else:
				shape = "rectangle"
		else:
			shape = "rhombus"

	#Pentagon - 5
	elif len(approx) == 5:
		shape = "pentagon"

	#Circle - no sides
	else:
		(x,y), r = cv.minEnclosingCircle(c)

		if cv.contourArea(c) == np.pi*r*r :
			shape = "circle"
		else:
			shape = "oval"

	return shape


img = cv.imread("shapes.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
ret, thresh = cv.threshold(blurred, 127, 255, cv.THRESH_BINARY)
contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)



#looping over the contours
for c in contours:
	#finding the center of the contour
	M = cv.moments(c)
	cX = int(M["m10"]/M["m00"])
	cY = int(M["m01"]/M["m00"])

	#shape = detect(c)

	cv.drawContours(img, [c], -1, (0, 255, 0), 2)
	#cv.circle(img, (cX, cY), 7, (255, 255, 255), -1)
	#cv.putText(img, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

	
	cv.imshow("Image", img)
	cv.waitKey(0)

