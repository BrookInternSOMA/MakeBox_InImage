import function

croplist = open("croplist.txt","r").readlines()
#print(croplist)


for data in croplist:
	datalist = data.split(',')
	print(datalist)
	crop_name = datalist[0]
	ori_name = datalist[1]
	cut_x = int(datalist[2])
	cut_y = int(datalist[3])

	function.makeResult(crop_name,ori_name,cut_x,cut_y)


	





	#makebox(img)
	
