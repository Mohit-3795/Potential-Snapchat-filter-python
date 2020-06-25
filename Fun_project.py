import numpy
import cv2
import time

first_frame = None

while True:

    video = cv2.VideoCapture(0)
    check, frame = video.read()

    gray = cv2.GaussianBlur(frame, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue
    #this will take the code back to the begining of the while loop

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 28, 255, cv2.THRESH_BINARY)[1]
    #thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    
    cv2.imshow("Gray", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold frame", thresh_frame)
   #cv2.imshow("colorframe", frame)
    
    key = cv2.waitKey(1)

    if key == ord('q'):
        break 

#print(a)

video.release( )
cv2.destroyAllWindows

