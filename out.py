
from socket import *
import time
import sys
import timeit
from threading import Thread
from time import sleep
rport = 25555
sport=25556
my_ip = ""
count = 0
uri = sys.argv[-1]
if "sha1_hash" in uri:
	hash = uri.partition("=")[-1]
else:
	hash = "**HASH**"
print "Searching for file with hash :" + hash
class client:
	def __init__(self,ip):
		self.s = socket()
		self.s.connect((ip,12345))
		print self.s.recv(1024)
	def get_file_info(ip,theHash):	
		self.s.send("info")
		sleep(0.05)
		self.s.send(theHash)
		self.file_size = int(s.recv(1000))
		self.file_name = s.recv(1000)
def config():
	try:
		file = open("C:/droplet/dpl/networks.txt  ", "r+")
	except:
		file = open("C:/droplet/dpl/networks.txt", "w+")
	networks = []
	data = "adf"
	while data != "":
		data = file.readline()
		data = data.strip(" \n")
		networks.append(data)
	print networks
	return networks[:-1]

running = True
def find(networks):
	for netip in networks:
		netbytes = netip.split(".")
		netbytes[-1] = 0
		receiver = socket(AF_INET, SOCK_DGRAM)
		tosend = str(netbytes[0]) + "." + str(netbytes[1]) + "." + str(netbytes[2]) + "."
		for i in xrange(1, 255):
			receiver.sendto("alive", (tosend + str(i), rport))
	print "Exit Find"
	running = False


def meet(drop_uri,send_hash):
	finder = socket(AF_INET, SOCK_DGRAM)
	finder.bind(('', sport))
	start = time.time()
	data = "t"
	global running
	avail_ip=[]
	print "Loop started"
	while (time.time() - start) < 10 and running:
		try:
			finder.settimeout(10)
			data, addr = finder.recvfrom(1024)
			print data,
			print addr
		except:
			pass
		if "available" in data:
			recv_hash = data.split(":")[1]
			if recv_hash == send_hash:
				print "Hash Available"
				avail_ip.append(addr[0])
		try:
			addr
		except NameError:
			pass
		else:
			if data == "alive":
				finder.sendto(drop_uri,addr)
	print "Exit meet"
	return avail_ip
	finder.close()
def down_into(file,toServer,start,end):
	file.seek(start)
	toServer.send("start="+str(start))
	sleep(0.01)
	toServer.send("end="+ str(end))
	data = toServer.recv(10000000)
	file.write(data)
	return len(data)
def get_file_info(ip,theHash):
	
	print s.recv(1023)
	s.send("info")
	sleep(0.05)
	s.send(theHash)
	file_size = int(s.recv(1000))
	file_name = s.recv(1000)
	if(file_size=="0"):
		return 0
	return (s,file_name,file_size)
networks = config()

i = Thread(target = find, args= (networks,))
i.start()
ips= meet(uri,hash)
for x in range(0,len(ips)):
	download(ips[x],hash,x,len(ips))
else:
	print "File Not Found"
sleep(3)
