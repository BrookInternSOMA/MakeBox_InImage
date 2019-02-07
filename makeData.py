import cv2
import numpy as np
import os, random

import function
from function import *

cropf = open("croplist.txt","w")
cropf.close()

wh_count = 0
while(wh_count<5):
	cropf = open("croplist.txt","a")
	wh_count = wh_count+1
	for img in allfiles(INPUT_DIR):
		new_name = cutFromOri(img)
		cropf.write(new_name+"\n")
	cropf.close()


	#makebox(img)
	
