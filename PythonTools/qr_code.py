

# pip install qrcode  
# pip install  image 
# pip install qr  
# pip install colorama 

import os

array = ['1','2','3']

for (index,a) in enumerate(array):
	os.system('qr %s >  店铺%s.png' % (a ,index+1))
	print('qr %s >  店铺%s' % (a ,index))


