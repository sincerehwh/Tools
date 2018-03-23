

使用？



import os 

filename = ".a"

types = ["armv7","arm64","i386","x86_64"]


def separate(filename):
	for order in types:
		operations = ""
		new_file_name = filename+"_"+order+".a"
		if order == "armv7" or "arm64":
			operations = "lipo "+filename+" -thin "+order+" -output "+ new_file_name
		else order == "i386":
			operations = "lipo -extract_family i386 -output " + new_file_name
		os.system(operations)


def combine(*filename):
	files = ""
	for file in filename:
		files +=  " " + file
	operations = "lipo -create" + files + " -output " + " combine.a"
	os.system(operations)


def showInfo(filename):
	os.system("lipo -info " + filename)



