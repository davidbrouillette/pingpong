from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (1920,1080)
camera.framerate = 15
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "TEST"
camera.start_preview(alpha=100)
sleep(5)
camera.stop_preview()