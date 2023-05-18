import cv2
cam = cv2.VideoCapture(0)
if (cam.isOpened() == False): 
  print("Unable to read camera feed")
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('enter id number : ')
count = 0
while(True):
    _,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame1', gray)
    faces = face_detector.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('frame', img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif count>100:
        break
cam.release()
print("Reading is completed for the person with id = " + face_id)
cv2.destroyAllWindows()
