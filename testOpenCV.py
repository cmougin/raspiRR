# -*- coding: utf-8 -*-
"""
premier essai reconnaissance de formes simples avec OpenCV - 10.10.2015
C. Mougin
"""

import cv2
import cv2.cv as cv
import numpy as np

print u"Début"
print "loading picture"
img = cv2.imread(u'carréRondTriangle.jpg')
print "converting to gray"
img = cv2.cvtColor(img, cv.CV_BGR2GRAY)
print "blurring it"
img = cv2.GaussianBlur(img,(15,15),0)

ret,th1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,15,4)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,15,4)

#http://docs.opencv.org/modules/imgproc/doc/feature_detection.html
# Python: cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) → circles
#    Parameters:	
#
#        image – 8-bit, single-channel, grayscale input image.
#        circles – Output vector of found circles. Each vector is encoded as a 3-element floating-point vector (x, y, radius) .
#        circle_storage – In C function this is a memory storage that will contain the output sequence of found circles.
#        method – Detection method to use. Currently, the only implemented method is CV_HOUGH_GRADIENT , which is basically 21HT , described in [Yuen90].
#        dp – Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.
#        minDist – Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.
#        param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller).
#        param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
#        minRadius – Minimum circle radius.
#        maxRadius – Maximum circle radius.

print "detecting circles"
circles = cv2.HoughCircles(th3,cv.CV_HOUGH_GRADIENT, 0.6, 100, param2=30, minRadius=110, maxRadius=500)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',th1)
cv2.waitKey(0)
cv2.imshow('image',th2)
cv2.waitKey(0)
cv2.imshow('image',th3)
cv2.waitKey(0)

print "affichage des cercles"
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    print "cercle de centre (%d, %d) et de rayon %d"%(i[0],i[1],i[2])
    cv2.circle(th3,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    #cv2.circle(th3,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('image',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()

print "Fin."