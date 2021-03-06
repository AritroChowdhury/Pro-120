import cv2
import numpy as np
import time

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = cap.read()
    bg = np.flip(bg, axis=1)

    bg = np.flip(bg, axis=1)

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break

frame=cv2.resize(frame,(640,480))
image=cv2.resize(frame,(640,480))

u_black=np.array([104,153,70])
l_black=np.array([30,30,0])

lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255,255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)