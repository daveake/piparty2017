import picamera, os

camera = picamera.PiCamera()

camera.resolution = (720, 480)

camera.capture('pic.jpg')

os.system('ssdv -e -c PISKY -i 1 pic.jpg pic.bin')