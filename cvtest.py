import cv2
import numpy as np
import os


OUTPUT_DIR = "./output/"
INPUT_DIR = "./input/"


def allfiles(path):
	flist = []
	for root, dirs, files in os.walk(INPUT_DIR):
		for file in files:
			flist.append(file)
	return(flist)
	
def makebox(imgname):
	ori_img = cv2.imread(INPUT_DIR+imgname)
	boximg = cv2.imread('box.png')

	ori_img = cv2.resize(ori_img, dsize=(256,256),interpolation=cv2.INTER_AREA)

	ysize_box = 70
	xsize_box = ysize_box * 2

	boximg = cv2.resize(boximg, dsize=(xsize_box, ysize_box), interpolation=cv2.INTER_AREA)

	xval = (256-xsize_box)/2
	yval = (256-ysize_box)/2
	print(xval)

	roi = ori_img[int(xval):int(xval)+xsize_box,int(yval):int(yval)+ysize_box]


	ori_img[int(yval):int(yval)+ysize_box,int(xval):int(xval)+xsize_box] = boximg
	
	cv2.imwrite(OUTPUT_DIR + imgname,ori_img)
	
	#cv2.imshow('result',ori_img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	#print(roi)



		
for img in allfiles(INPUT_DIR):
	makebox(img)
