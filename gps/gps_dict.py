import socket, json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 6005))                               		

while True:
	reply = s.recv(4096)                                     
	if reply:
		inputstring = reply.split(b'\n')
		for line in inputstring:
			if line:
				temp = line.decode('utf-8')
				j = json.loads(temp)
				print(j)
				print("Your position is %.5f,%.5f" % (j['lat'],j['lon']))
