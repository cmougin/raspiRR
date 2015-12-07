# -*- coding: utf-8 -*-
"""
premier essai reconnaissance de formes simples avec OpenCV - 10.10.2015
C. Mougin
"""

import cv2
import cv2.cv as cv
import numpy as np

print u"Début"
img = cv2.imread(u'carréRondTriangle.jpg',1)
img2 = cv2.cvtColor(img, cv.CV_BGR2GRAY)
img2 = cv2.GaussianBlur(img2,(9,9),2,2)

circles = cv2.HoughCircles(img2, cv.CV_HOUGH_GRADIENT, 1, 100, #img2.row/8,
                           200, 100, 0, 0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    #cv2.circle(th3,(i[0],i[1]),2,(0,0,255),3)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print "Fin."