import picamera
import datetime as dt
import os

# Make sure we have a folder for storing the images
if not os.path.exists('recordings'):
    os.makedirs('recordings')


camera = picamera.PiCamera(resolution=(800, 600), framerate=24)
#camera = picamera.PiCamera(resolution=(640, 480), framerate=24)
#camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
#camera.vflip = True

camera.start_preview()
camera.annotate_background = picamera.Color('black')
camera.annotate_text_size = 16
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.start_recording('recordings/recording_' + dt.datetime.now().strftime('%Y%m%d_%H%M') +'.h264', quality=25)

for i in range (2, 10):
    start = dt.datetime.now()
    while (dt.datetime.now() - start).seconds < 600:
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(0.2)
    #camera.split_recording('recordings/timestamped-%d.h264' % i)
    camera.split_recording('recordings/recording_' + dt.datetime.now().strftime('%Y%m%d_%H%M') +'.h264')

camera.stop_recording()

