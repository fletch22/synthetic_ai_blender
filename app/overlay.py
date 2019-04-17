# USAGE
# python overlay.py

# import the necessary packages
from __future__ import print_function
import numpy as np
import cv2
import os
from app.config import config
import logging

image_orig_path1 = os.path.join(config.SYNTH_IMAGES_PATH, "monkey_0-0_0_0.png")
image_orig_path2 = os.path.join(config.SYNTH_IMAGES_PATH, "monkey_1-1.18_0.15_2.81.png")


logging.info(image_orig_path1)


def run():
	# load the image
	image1 = cv2.imread(image_orig_path1)
	overlay = cv2.imread(image_orig_path2)

	# loop over the alpha transparency values
	# for alpha in np.arange(0, 1.1, 0.1)[::-1]:

	alpha = .5
	# create two copies of the original image -- one for
	# the overlay and one for the final output image
	# overlay = image1.copy()
	output = image1.copy()

	# draw a red rectangle surrounding Adrian in the image
	# along with the text "PyImageSearch" at the top-left
	# corner
	# cv2.rectangle(overlay, (420, 205), (595, 385),
	# 	(0, 0, 255), -1)
	# cv2.putText(overlay, "PyImageSearch: alpha={}".format(alpha),
	# 	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

	# rows, cols, channels = overlay.shape
	# overlay = cv2.addWeighted(image1[250:250 + rows, 0:0 + cols], 0.5, overlay, 0.5, 0)

	# apply the overlay
	cv2.addWeighted(overlay, alpha, output, 1 - alpha,
		0, output)

	# show the output image
	print("alpha={}, beta={}".format(alpha, 1 - alpha))
	cv2.imshow("Output", output)
	cv2.waitKey(0)