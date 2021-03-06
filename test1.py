# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# ap.add_argument("-w", "--width", type=float, required=True,
# 	help="width of the left-most object in the image (in inches)")
# args = vars(ap.parse_args())
image_name = "/lhome/risverm/Pictures/necklace.jpeg"
# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(image_name)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# sort the contours from left-to-right and initialize the
# 'pixels per metric' calibration variable
cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
cv2.imshow("image", image)
cv2.waitKey(0)
# orig = image.copy()
# (cnts, _) = contours.sort_contours(cnts)
# pixelsPerMetric = None
# # loop over the contours individually
# for c in cnts:
# 	# if the contour is not sufficiently large, ignore it
# 	if cv2.contourArea(c) < 100:
# 		continue
# 	# compute the rotated bounding box of the contour
#
# 	box = cv2.minAreaRect(c)
# 	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
# 	box = np.array(box, dtype="int")
# 	# order the points in the contour such that they appear
# 	# in top-left, top-right, bottom-right, and bottom-left
# 	# order, then draw the outline of the rotated bounding
# 	# box
# 	box = perspective.order_points(box)
# 	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
# 	# loop over the original points and draw them
# 	for (x, y) in box:
# 		cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
# cv2.imshow("image", orig)
# cv2.waitKey(0)