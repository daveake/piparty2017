from gpiozero import OutputDevice
import serial

enable_pin = OutputDevice(17)
enable_pin.on()

rtty_serial = serial.Serial()
rtty_serial.port = '/dev/ttyAMA0'
rtty_serial.baudrate = 50
rtty_serial.stopbits = 2
rtty_serial.bytesize = 7
rtty_serial.open()

while True:
	rtty_serial.write('Hello World\n'.encode())
