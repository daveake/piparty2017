PacketCount = 0
with open('pic.bin', mode='rb') as file:
	while True:
		packet = file.read(256)
		if packet:
			PacketCount += 1
		else:
			break
			
print('There were ' + str(PacketCount) + ' packets')
