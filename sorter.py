# Author: Max Cowan 2017

import cv2 as cv
import numpy as np
import colorsys as clr
import os
import operator
import shutil


# Returns 3 values for average Hue, Saturation, and Value
def findAvgHSV(filename, path):

    file_path = path + filename   # Construct file path
    cover = cv.imread(file_path)  # Read file

    avgRowColor = np.average(cover, axis=0)  # Find the average color for all rows

    avgOverallColor = np.average(avgRowColor, axis=0)  # Find average color of all averaged rows

    avgRGB = np.uint8(avgOverallColor)  # Round to integer values

    avgHSV = clr.rgb_to_hsv(avgRGB[0], avgRGB[1], avgRGB[2])  # Convert to HSV format

    return avgHSV


# Main code

# Path where initial cover images are saved
IMAGE_PATH = "Cover_Images/"
# Path where sorted cover images are saved
SORTED_PATH = "Sorted_Cover_Images/"

# This will hold album name as the key, and average HSV information as the value
colorDict = {}

# Traverse the downloaded covers
for cover_image in os.listdir(IMAGE_PATH):
    if cover_image.endswith(".jpg"):
        colorDict[cover_image] = findAvgHSV(cover_image, IMAGE_PATH)  # Populate dictionary

# Sort the cover images by HSV
sortedByHue = sorted(colorDict.items(), key=operator.itemgetter(1))

# Copy the files with ordered file names to the sorted directory
for i in range(len(sortedByHue)):
    src_path = IMAGE_PATH + sortedByHue[i][0]
    dst_path = SORTED_PATH + str(len(sortedByHue)-i) + "_" + sortedByHue[i][0]
    shutil.copyfile(src_path, dst_path)




