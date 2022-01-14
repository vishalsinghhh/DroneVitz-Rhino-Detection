import cv2
import numpy as np

frame = cv2.imread('Resources/nohornRhino.jpeg')
hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# Blood Color
low_red = np.array([161, 155, 84])
high_red = np.array([179,255,255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)    
red = cv2.bitwise_and(frame, frame, mask=red_mask)

cv2.imshow("img", frame)
cv2.imshow("Red mask", red)
cv2.waitKey(0)