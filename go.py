import os ,time
import mod_vpn2
mod_vpn2.fnc_vpn ()



def check():
	with open("log.txt") as fil:
		data_file=fil.readlines()
	for lines in data_file:
		if "API Error: Network Unusable" in lines :
			print("FuCkkkk !!!!!!!")
			print(mod_vpn2.random_vpn)
		if "Honeygain service is connected and running" in lines:
			print("ok ok ok ok o k o k o k")




def start():
	os.system("sh -c './honeygain -tou-accept -email y0shimitsugh0st84@gmail.com -pass testpassw0rd -device DEVICE_PNV_SYD' 2>&1 | tee log.txt &")
	time.sleep(5)
	print("ok")
	check()






start()