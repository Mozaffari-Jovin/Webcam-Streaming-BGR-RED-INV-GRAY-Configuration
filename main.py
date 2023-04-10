import cv2
import numpy as np

import time
t0 = time.time()

cap = cv2.VideoCapture(0)  # 0 coresponds to the laptop webcam and 1 to the one from USB

# cap is an object and VideoCapture is a class
# the cap's method has two output: ret and frame

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
fps = cap.get(cv2.CAP_PROP_FPS)
print(width, height, fps) # frame per second
# quit()

while True:
	ret, frame = cap.read()
	if ret:
		frame_BGR = cv2.flip(frame, 1) # move column by 180 deg
		
		frame_RED = frame_BGR.copy()
		frame_RED[:, :, 2] = 255 # change the red matrix (BGR) to 255 that is red is dominant
		
		frame_INV = 255 - frame_BGR # changes color of each pixel
		
		frame_GRAY2D = cv2.cvtColor(frame_BGR, cv2.COLOR_BGR2GRAY)
		frame_GRAY = np.zeros((int(height), int(width), 3))
		frame_GRAY[:, :, 0] = frame_GRAY2D
		frame_GRAY[:, :, 1] = frame_GRAY2D
		frame_GRAY[:, :, 2] = frame_GRAY2D
		frame_GRAY = frame_GRAY.astype(np.uint8)

		# print(frame_BGR.shape, frame_RED.shape, frame_INV.shape, frame_GRAY.shape)
		# quit()
		frame_concat_0 = np.concatenate([frame_BGR, frame_INV], 0)   
		frame_concat_1 = np.concatenate([frame_RED, frame_GRAY], 0)
		frame_concat = np.concatenate([frame_concat_0, frame_concat_1], 1)
		frame_concat_resize = cv2.resize(frame_concat, (400, 300)) # resize the frame

		t1 = time.time() - t0
		t1_str = str(round(t1, 2))
		cv2.putText(frame_concat_resize, t1_str, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, \
			1, (0, 0, 255), 1)
		cv2.putText(frame_concat_resize, "Soheil Mozaffari", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, \
			1, (0, 255, 255), 1)

		cv2.imshow("myWebcam", frame_concat_resize)
		q = cv2.waitKey(1)
		if q == ord("q"):
			break

cv2.destroyAllWindows() # this function allows users to destroy or close all windows at any time after exiting the script.
cap.release() # close cap



