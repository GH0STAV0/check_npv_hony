import os ,time
import mod_vpn2

import string
import random





def id_generator(size=6, chars=string.ascii_uppercase + string.digits):

	return ''.join(random.choice(chars) for _ in range(size))




mod_vpn2.fnc_vpn ()

def save_succed(logg):
	with open("succed_nord",'a') as fw:
		fw.write(logg+"\n")

def check2():
	with open("log.txt") as fil:
		data_file=fil.readlines()
	for lines in data_file:
		if "Honeygain service is connected and running" in lines:
			print("ok ok ok ok o k o k o k")
			save_succed(mod_vpn2.arry_1[0])





def check():
	with open("log.txt") as fil:
		data_file=fil.readlines()
	for lines in data_file:
		if "API Error: Network Unusable" in lines :
			print("FuCkkkk !!!!!!!")
			print(mod_vpn2.arry_1)
		if "Honeygain service is starting" in lines:
			time.sleep(15)
			check2()
	os.system("pkill openvpn && pkill honeygain && rm log.txt ipifo.json")




def start():
	iid=id_generator()
	print(iid)
	os.system("sh -c './honeygain -tou-accept -email y0shimitsugh0st84@gmail.com -pass testpassw0rd -device DEVICE_PNV_TEST0"+iid+"' 2>&1 | tee log.txt &")
	time.sleep(5)
	print("ok")
	check()






start()