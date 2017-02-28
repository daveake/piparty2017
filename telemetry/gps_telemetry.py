import socket, json, crcmod

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 6005))                               		

SentenceCount = 0
while True:
	reply = s.recv(4096)                                     
	if reply:
		inputstring = reply.split(b'\n')
		for line in inputstring:
			if line:
				temp = line.decode('utf-8')
				position = json.loads(temp)
				
				SentenceCount += 1
				
				values = ['PIPARTY', SentenceCount, position['time'],
						  '{:.5f}'.format(position['lat']),
						  '{:.5f}'.format(position['lon']),
						  int(position['alt'])]
						  
				temp = ','.join(map(str, values))
				
				crc16 = crcmod.predefined.mkCrcFun('crc-ccitt-false')
				crc_string = hex(crc16(temp.encode()))[2:].upper().zfill(4)
				
				sentence = '$$' + temp + '*' + crc_string + '\n'

				print(sentence)
