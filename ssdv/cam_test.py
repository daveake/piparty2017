import picamera

camera = picamera.PiCamera()

camera.resolution = (720, 480)				

camera.capture('pic.jpg')
