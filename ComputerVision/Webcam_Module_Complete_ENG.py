'''
Video Capturing Module
Commands:
- Key "b": Black & White
- Key "t": Time (Date and hour)
- Key "s": Snapshot (jpg)
- Key SPACE: Video Recording (AVI 480x360)
- Key "q": Quit
'''

import cv2
from datetime import datetime

rec = False
bg_mode = False
dt_mode = False

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'MJPG')
out = None

available, _ = cap.read()

# Exit if webcam not available
if (not available):
    print("Webcam not available")
    exit(0)

while(cap.isOpened()):

    _, frame = cap.read()

    if(bg_mode):
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if(dt_mode):
        now = datetime.now()
        str_now = now.strftime("%d/%m/%Y %H:%M:%S")
        cv2.putText(frame, str_now, (20,frame.shape[0]-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,255), 2)

    if(rec):
        out.write(frame)
        cv2.circle(frame, (frame.shape[1]-30, frame.shape[0]-30), 10, (0,0,255), cv2.FILLED)

    cv2.imshow("Rosario Moscato Lab Webcam",frame)
    k = cv2.waitKey(1)

    if(k==ord("b")):
        bg_mode = not bg_mode
        print("Black & White Mode: %s" % bg_mode)
    
    if(k==ord("t")):
        dt_mode = not dt_mode
        print("Show Time: %s" % dt_mode)

    if(k==ord("s")):
        now = datetime.now()
        filename = now.strftime("%Y%m%d%H%M%S")+".jpg"
        cv2.imwrite(filename, frame)
        print("Screenshot: %s" % (filename))
    
    if(k==ord(" ")):
        if(out==None):
            now = datetime.now()
            filename = now.strftime("%Y%m%d%H%M%S")+".avi"
            out = cv2.VideoWriter(filename, codec, 24., (640,480))
        rec = not rec
        print("Video Recording: %s %s" % (filename, rec))

    if (k==ord("q")): #ord() returns the ASCII code of a char
        break

if(out!=None):
    out.release()

cap.release() #webcam releasing (make it free for others)
cv2.destroyAllWindows()


