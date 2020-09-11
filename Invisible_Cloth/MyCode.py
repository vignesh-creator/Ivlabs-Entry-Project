import numpy as np
import cv2
cap = cv2.VideoCapture(0)
wid=int(cap.get(3))
height=int(cap.get(4))
size=(wid,height)
out = cv2.VideoWriter('vid.avi',cv2.VideoWriter_fourcc(*'DIVX'),20,size)
if not cap.isOpened():
    print("Cannot Open Camera")
    exit()
i=0
while(i<30):
    ret,bg=cap.read()
    i+=1
bg = np.flip(bg,axis=1)
while (True):
    ret, frame = cap.read()
    if ret == False:
        print("Can't receive frame")
        break
    frame = np.flip(frame, axis=1)
    bgr_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([94, 80, 2])
    upper = np.array([126, 255, 255])
    mask = cv2.inRange(bgr_hsv, lower, upper)
    bitwise1 = cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(mask))
    bitwise2 = cv2.bitwise_and(bg,bg,mask=mask)
    output = cv2.addWeighted(bitwise1,1,bitwise2,1,0)
    out.write(output)
    cv2.imshow("Invisible!", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

