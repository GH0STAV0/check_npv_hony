import os ,random ,subprocess,time 

import cnf_bvb
# import socket

# hostname= socket.getfqdn()

########################### VPN  #############################/N0RD/WORKING_CONFIG/

# file_list_1='NORD_list_1'
file_list_1='NCH_list_1'
# 
# telrgram_vpn_text=[]



pwd = os.path.dirname(os.path.realpath( __file__ ))

vpn_folder=pwd+"/CHEAP_VPN/"
# vpn_folder=pwd+"/N0RD/WORKING_CONFIG/"
all_vpn_config_file=os.listdir(vpn_folder)


file_vpn_dead=cnf_bvb.file_vpn_dead
p_vpn_dead=cnf_bvb.p_vpn_dead

##############################################################

def check_list_vpn_lengh():
	num_lines = sum(1 for line in open(file_list_1))
	if num_lines==0:
		creat_list_of_vpn()
	else:
		pass

##############################################################

def creat_list_of_vpn():
	with open(file_list_1,'w') as fw:
		for i in all_vpn_config_file:
			fw.write(i+"\n")

##############################################################

def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines

##############################################################

def write_new_list(new_vpn_arry):
	with open(file_list_1,"w") as fw:
		for i in new_vpn_arry:
			fw.write(i)
	print("OK !!")

##############################################################

def remove_from_list_running(vpn_name):
	print("REMOVING THE VPN CONFIG [ "+vpn_name+" ]",end=' ',flush=True)
	vpn_name=vpn_name+"\n"
	arry_vpn_list=read_current_list_vpn()
	arry_vpn_list.remove(vpn_name)
	write_new_list(arry_vpn_list)

##############################################################

def get_random_vpn():
	check_list_vpn_lengh()
	arry_vv=read_current_list_vpn()
	random_vpn=random.choice(arry_vv)
	random_vpn=random_vpn.replace('\n','')
	final_vpn=vpn_folder+random_vpn
	# print(random_vpn)
	return final_vpn , random_vpn

##############################################################



def fnc_vpn():

	final_vpn,random_vpn=get_random_vpn()
	print("###################################################")
	print("KILLING OPENVPN ....",end=' ')
	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	time.sleep(3)
	os.system("rm -rf /var/log/openvpn/openvpn.log")
	time.sleep(1)
	os.system("touch /var/log/openvpn/openvpn.log")
	print ("OK !!!!!")
	print("STARTING VPN " , end="")
	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',final_vpn , '--log' , '/var/log/openvpn/openvpn.log'])
	remove_from_list_running(random_vpn)
	time.sleep(15)
	print("["+random_vpn+"]" , end="")
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
		if logfile.read().find('Sequence Completed') !=-1:
			print ("OK !!!!!")
			ac_ip,tz,loc=cnf_bvb.iip()
			os.environ['TZ'] = tz
			meddas="VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip+"||"+ tz
			print(meddas)
			cnf_bvb.send_msg(meddas)
			return [x ,True]
		else :
			print("")
			print("VPN STATUS = OFF || "+ random_vpn )
			fnc_vpn ()
			return [x ,False]

	time.sleep(5)
	os.system("echo '' > /var/log/openvpn/openvpn.log")



	

########################################################################################################################################


################################

#cnf_bvb.testt()
# fnc_vpn ()