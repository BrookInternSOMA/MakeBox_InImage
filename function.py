import cv2
import numpy as np
import os, random

INPUT_DIR = "./original/"
CROP_DIR = "./crop/"
AFTER_GAN_DATA = "./afterGAN/"
OUTPUT_DIR = "./output/"

count = 0
boximg = cv2.imread('box.png')
BOXSIZE = 256

def allfiles(path):
	flist = []
	f = open("file_list.txt","w")
	for root, dirs, files in os.walk(INPUT_DIR):
		for file in files:
			flist.append(file)
	for i in flist:
		f.write(i)
		f.write('\n')

	return(flist)
	
def makebox(imgname): #이미지 읽어서 바로
	ori_img = cv2.imread(INPUT_DIR+imgname)
	global boximg

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

def makeboxFromCut(img,img_info): #이미지 파일 받아서
	#ori_img = cv2.imread(INPUT_DIR+imgname)
	#boximg = cv2.imread('box.png')
	global count, boximg
	count = count + 1

	new_img = cv2.resize(img, dsize=(256,256),interpolation=cv2.INTER_AREA)

	ysize_box = random.randrange(50,90) #상자 크기
	xsize_box = ysize_box * 2

	boximg = cv2.resize(boximg, dsize=(xsize_box, ysize_box), interpolation=cv2.INTER_AREA)

	xval = (256-xsize_box)/2
	yval = (256-ysize_box)/2
	print(xval)

	roi = new_img[int(xval):int(xval)+xsize_box,int(yval):int(yval)+ysize_box]


	new_img[int(yval):int(yval)+ysize_box,int(xval):int(xval)+xsize_box] = boximg
	
	new_name =  str(count).zfill(5) + "_" + img_info[0]
	cv2.imwrite(CROP_DIR + new_name,new_img)

	return new_img, new_name

	

def cutFromOri(ori_img): #사진에서 랜덤으로 크롭, 256 256 만들어줌

	img = cv2.imread(INPUT_DIR+ori_img)
	re_img = cv2.resize(img, dsize=(768,768),interpolation=cv2.INTER_AREA)
	img_info = [] #0:name 1:cut xs 2:cut y
	img_info.append(ori_img)
	print(img.shape[1])
	cut_x = random.randrange(1,512)
	img_info.append(cut_x)
	cut_y = random.randrange(1,512)
	img_info.append(cut_y)

	print(cut_x)
	print(cut_y)

	crop_img = re_img[cut_x:cut_x+256,cut_y:cut_y+256] #왼쪽 위가 0,0
	
	new_img, new_name = makeboxFromCut(crop_img,img_info)
	new_name = new_name + ',' + img_info[0] + ',' + str(img_info[1]) + ',' + str(img_info[2])
	#makeResult(re_img,new_img,img_info)

	#cv2.imshow("Crop",crop_img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	return new_name		


def makeResult(new_img_name,ori_img_name,cut_x,cut_y): #큰 이미지에 합체
	

	ori_img = cv2.imread(INPUT_DIR+ori_img_name)
	ori_img = cv2.resize(ori_img, dsize=(768,768),interpolation=cv2.INTER_AREA)
	new_img = cv2.imread(AFTER_GAN_DATA+new_img_name)

	#ori_img[cut_y:cut_y+BOXSIZE,cut_x:cut_x+BOXSIZE] = new_img
	ori_img[cut_x:cut_x+BOXSIZE,cut_y:cut_y+BOXSIZE] = new_img

	cv2.imwrite(OUTPUT_DIR + new_img_name,ori_img)
	#cv2.imshow("Crop",ori_img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
