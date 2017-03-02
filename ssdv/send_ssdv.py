from lora import *
import time

mylora = LoRa(Channel=0, Frequency=434.450, Mode=1)

PacketCount = 0
with open('pic.bin', mode='rb') as file:
	while True:
		packet = file.read(256)
		if packet:
			PacketCount += 1
			print('Sending packet  ' + str(PacketCount))
			mylora.send_packet(packet[1:])
			while mylora.is_sending():
				time.sleep(0.1)
			print('Sent')
		else:
			break