

# 
#
# 

import os
import time

# 参考 https://blog.csdn.net/yepiaouang/article/details/79353377
# 参考 https://blog.csdn.net/liyun123gx/article/details/50774485

# 使用方法：
#	1.将.a 文件和 本文件放到同一个文件中
#	2.在终端输入: python3  static_lib_separation.py 
#	3.回车，OK!
# 


def separate(filename):
	types = ["armv7","arm64","i386","x86_64"]
	if len(filename.split(".")) != 2:
		print("输入正确的文件！！！")
		return
	for order in types:
		print("正在拆分：" + filename + " " + order + "的静态库....")
		operations = ""
		new_file_name = filename.split(".")[0] +"_"+order+".a"
		if order == "armv7" or "arm64":
			operations = "lipo "+filename+" -thin "+order+" -output "+ new_file_name
		elif order == "i386" or "x86_64":
			operations = "lipo -extract_family i386 -output " + new_file_name
		os.system(operations)
		showInfo(new_file_name)


def combine(*filename):
	files = ""
	for file in filename:
		files +=  " " + file
	operations = "lipo -create" + files + " -output " + " combine.a"
	os.system(operations)
	showInfo("combine.a")


def showInfo(filename):
	os.system("lipo -info " + filename)
	print( filename + "拆分成功！！！")


def trans_afile_to_mfile(filename):
	os.system("ar -x " + filename)
	time.sleep(3)
	os.system("ls > names.txt ")
	time.sleep(3)
	with open("names.txt",'r') as f:
		while  True:
			line = f.readline()
			if not line:
				break
				pass
			filename = line.split(".")[0]
			command = "nm "+ filename + ".o" + " > " + "__OC__"+filename+".m"
			os.system(command)

# 输入文件名
separate("filename.a")         

# 输入要合并的文件
combine("_armv7.a","_arm64.a")

# 将.a文件拆解成.o
# 传入arm64的文件名
# 在终端运行
trans_afile_to_mfile("coinapi_arm64.a")




