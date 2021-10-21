import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #cv2.imshow('Input', frame)
    face_cascade=cv2.CascadeClassifier(r"C:\Users\hp\Desktop\dt project\eye contact code.xml")
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=80)
    ar=len(eyes)
    if ar==0:
        print("maintain eye contact")
    else:
        for x,y,w,h in eyes:
            frame=cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,0),8)
    cv2.imshow("gray", frame)
    cv2.waitKey(1000)
    c = cv2.waitKey(1)
    if c == 5:
        break
    

cap.release()
cv2.destroyAllWindows()