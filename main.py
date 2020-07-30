import cv2
import numpy as np
import time

print("Welcome to World Of becoming Invisible \n")
print('Press "Esc", "q" or "Q" to exit.')
print('\nBy : Anmol Srivastava')

# define a video capture object 
cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0

for i in range(30):
	# Capture frame-by-frame
	ret, background = cap.read()

#Flip the color bits for the first capture
background = np.flip(background,axis = 1)

while(cap.isOpened()):
	ret, img = cap.read()
	imp = np.flip(img, axis = 1)

	# Our operations on the frame come here
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	# apply guassian blur on src - hsv image
	blur = cv2.GaussianBlur(hsv, (35, 35), 0)

	#hsv color value from lower red to upper red
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])

	#mask the color from lower red to upper red
	mask1 = cv2.inRange(hsv,lower_red,upper_red)

	#For deection of color from lower red to upper red

	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])

	#making the color from lower red to upper red
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	#adding the mask to generate a final mask

	mask = mask1 + mask2
	#removing the noise by first erosion then follwed by dilation both by the use of MORPH_OPEN, by erosion on a 5 X 5 kernel 
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))

	img[np.where(mask == 255)] = background[np.where(mask == 255)]

	# Window Named to Invisiblity Cloak
	# will display the masked image img
	cv2.imshow('Invisiblity Cloak', img)

	ch = cv2.waitKey(1)
	if ch == 27 or ch == ord('q') or ch == ord('Q'):
		break

print('Thank You For Becoming invisible and trying out the INVISIBILITY CLOAK')
print('BYE')
time.sleep(10)