#!/bin/usr/python36

import os
import cv2


cap = cv2.VideoCapture(0)
ret , photo = cap.read()
m = raw_data("Enter the path for saving the captured picture")
cv2.imwrite( m ,photo)