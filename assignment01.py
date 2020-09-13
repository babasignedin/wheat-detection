import cv2 
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors

nemo = cv2.imread("B:\\Project\\fish\\nemo4.jpg") #for inputting the image
plt.imshow(nemo) #for plotting the image
plt.show() #for plotting the image


#openCV by default takes input images in BGR format.
#But our original image is encoded in BGR. So to show the original
# image, we have to convert it to BGR. 
nemo_rgb = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
plt.imshow(nemo_rgb)
plt.show()

#convert to grayscale image
nemo_bg = cv2.cvtColor(nemo, cv2.COLOR_BGR2GRAY)
plt.imshow(nemo_bg)
plt.show()
#cv2.imshow('Gray image', nemo2)
#cv2.waitKey()

#convert to binary(black and white) image
#Each pixel in a grayscale image has value between 0(black) to 255(white)
#Pick threshold = 127 
(thresh, nemo_bw) = cv2.threshold(nemo_bg, 127, 255, cv2.THRESH_BINARY)
#converts all pixel <= 127 to 0
#converts all pixel > 127 to 255
#That why any pixel of the image will be either 0 or 255. That's a binary image

cv2.imshow("bw", nemo_bw)
cv2.waitKey(0)
plt.imshow(nemo_bw)
plt.show()


#convert to HSV image
nemo_hsv = cv2.cvtColor(nemo, cv2.COLOR_BGR2HSV)
plt.imshow(nemo_hsv) 
plt.show()

#convert to LAB format
nemo_lab = cv2.cvtColor(nemo,cv2.COLOR_BGR2LAB)
plt.imshow(nemo_lab) 
plt.show()

#convert to HSL format
nemo_hsl = cv2.cvtColor(nemo,cv2.COLOR_BGR2HLS)
plt.imshow(nemo_hsl) 
plt.show()


#convert to YCrCb format
nemo_ycrcb = cv2.cvtColor(nemo,cv2.COLOR_BGR2YCrCb)
plt.imshow(nemo_ycrcb) 
plt.show()