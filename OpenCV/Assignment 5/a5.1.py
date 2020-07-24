import cv2 as cv
import numpy as np

cap = cv.VideoCapture('football_video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5,5), 0)
	ret, thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3.5)
	contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)


cap.release()
cv2.destroyAllWindows()


	
