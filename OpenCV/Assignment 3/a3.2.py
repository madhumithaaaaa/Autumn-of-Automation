import cv2 as cv 
import sys

def dodgeV2(image, mask):
	return cv.divide(image, 255-mask, scale=256)

def burnV2(image, mask):
	return 255 - cv.divide(255-image, 255-mask, scale=256)

cap = cv.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	frame_gray_inv = 255 - frame_gray

	frame_blur = cv.GaussianBlur(frame_gray_inv, ksize=(21,21), sigmaX=0, sigmaY=0)

	pencil_sketch = dodgeV2(frame_gray, frame_blur)
	#pencil_sketch = cv.Laplacian(frame, cv.CV_64F)

	flipped = cv.flip(pencil_sketch, 1)
	cv.imshow('frame', flipped)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
'''k = cv.waitKey(0)
if k == ord('s'):
	cv.imwrite("Pencil Sketch", pencil_sketch)'''

cv.destroyAllWindows()