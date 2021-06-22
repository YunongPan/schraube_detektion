#!/usr/bin/env python
import cv2  
import numpy as np 
import matplotlib.pyplot as plt


frame = cv2.imread("./DSC00017.jpg")

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_red = np.array([1,0,120])
upper_red = np.array([180,255,255])
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)
img_Guassian = cv2.GaussianBlur(res,(21,21),0)

img = cv2.cvtColor(img_Guassian, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
cimg = frame.copy()

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 40, 60, 200)
print(circles)
if len(circles) is not 0:
    a, b, c = circles.shape
    print(str(circles))
    for i in range(b):
        print(circles[0][i][0])
        print(circles[0][i][1])
        cv2.circle(cimg, (int(circles[0][i][0]), int(circles[0][i][1])), 200, (255, 0, 0), 10)

plt.imshow(cimg)
plt.show()




