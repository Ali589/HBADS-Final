import cv2
import numpy

# Open the ZED camera
cap = cv2.VideoCapture(0)
if cap.isOpened() == 0:
    exit(-1)

# Set the video resolution to HD720 (2560*720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True :
    # Get a new frame from camera
    retval, frame = cap.read()
    # Extract left and right images from side-by-side
    left_right_image = numpy.split(frame, 2, axis=1)
    # Display images
    cv2.imshow("frame", frame)
    #cv2.imshow("right", left_right_image[0])
    #cv2.imshow("left", left_right_image[1])
    if cv2.waitKey(30) >= 0 :
        break

exit(0)
#import cv2

#cam = cv2.VideoCapture(1)
##       key value
#cam.set(3 , 640  ) # width
#cam.set(4 , 480  ) # height
#cam.set(10, 128  ) # brightness     min: 0   , max: 255 , increment:1
#cam.set(11, 50   ) # contrast       min: 0   , max: 255 , increment:1
#3cam.set(12, 70   ) # saturation     min: 0   , max: 255 , increment:1
#cam.set(13, 13   ) # hue
#cam.set(14, 50   ) # gain           min: 0   , max: 127 , increment:1
#cam.set(15, -3   ) # exposure       min: -7  , max: -1  , increment:1
#cam.set(17, 5000 ) # white_balance  min: 4000, max: 7000, increment:1
#cam.set(28, 0    ) # focus          min: 0   , max: 255 , increment:5
#cap = cam.read()