#!/usr/bin/env python
import cv2  
import numpy as np 
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('decke-schaube.mp4')

frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,0,120])
    upper_red = np.array([180,50,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame,frame, mask= mask)
    img_Guassian = cv2.GaussianBlur(res, (41, 41), 0)
    img_Gray = cv2.cvtColor(img_Guassian, cv2.COLOR_BGR2GRAY)

    cimg = frame.copy()

    circles = cv2.HoughCircles(img_Gray, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 20, 150)
    if len(circles) is not 0:
        a, b, c = circles.shape
        for i in range(b):
            cv2.circle(cimg, (int(circles[0][i][0]), int(circles[0][i][1])), 50, (255, 0, 0), 20)
            cv2.circle(cimg, (int(circles[0][i][0]), int(circles[0][i][1])), 5, (0, 0, 255), 20)

    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 1000,1000)
    cv2.imshow('image',cimg)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()





