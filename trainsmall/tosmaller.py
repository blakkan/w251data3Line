import cv2
import glob, os
for filename in glob.glob("../train/*.jpg"):
    shortfile = filename.split('/')[-1]
    print(shortfile)
    image = cv2.imread(filename)
    image2 = cv2.resize(image,(128,96))
    cv2.imwrite(shortfile, image2)
