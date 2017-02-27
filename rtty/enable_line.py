from gpiozero import OutputDevice
from time import sleep

enable_pin = OutputDevice(17)

while True:
	print ("HIGH")
	enable_pin.on()
	sleep(1)
	
	print ("LOW")
	enable_pin.off()	
	sleep(1)
