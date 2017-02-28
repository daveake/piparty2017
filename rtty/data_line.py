from gpiozero import OutputDevice
from time import sleep

enable_pin = OutputDevice(17)
enable_pin.on()

data_pin = OutputDevice(14)

while True:
	print ("HIGH")
	data_pin.on()
	sleep(1)
	
	print ("LOW")
	data_pin.off()	
	sleep(1)
