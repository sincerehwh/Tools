
import os
import platform

# 判断平台
def install_pip3():
	system_type = platform.system()
	if system_type == "Linux":
		os.system('sudo apt-get update')
		os.system('sudo apt-get install -U python3-pip')	
	elif system_type == 'Darwin':
		os.system('brew install pip3')


def install_libraries(libraries):
	pip3_install = "pip3 install "	
	for library in libraries:
		os.system(pip3_install+library)

# 安装初级包
python_base_libraries = ['numpy','scipy','pandas','matplotlib']
# 安装高级包
python_adve_libraries = ['nltk','python-igraph','scikit-learn']


install_libraries(python_base_libraries)
install_libraries(python_adve_libraries)


