import cv2 as cv

# 1.2

cap = cv.VideoCapture(0)

while(True):
	#Capture frame by frame
	ret, frame = cap.read()

	#Converting each frame to grayscale
	gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	'''To flip the image :
		flipcode = 0: flip vertically
		flipcode > 0: flip horizontally
		flipcode < 0: flip vertically and horizontally'''

	flipped = cv.flip(gray_vid, 1)

	cv.imshow('frame', flipped)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()

#cv.waitKey(0)
cv.destroyAllWindows()