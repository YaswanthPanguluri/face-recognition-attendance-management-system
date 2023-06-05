import cv2
import time
import numpy as np
import time
import datetime

#import excelsheet
import xlwt
from xlwt import Workbook 

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

from smtplib import SMTPException

#------------------------------------------------------------------------------------------

def send_an_email():
    toaddr = '*********@gmail.com'    
    from_mail_id = '****@gmail.com' 
    from_password = "*******"
    subject = "Attendance Report "

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_mail_id
    msg['To'] = toaddr
    msg.preamble = "test " 
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("xlwt example.xls", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="xlwt example.xls"')
    msg.attach(part)
    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(user = from_mail_id, password = from_password)
       #s.send_message(msg)
       print("--------  Sending mail please wait  ----------"+'\n')
       s.sendmail(from_mail_id, toaddr, msg.as_string())
       s.quit()
       time.sleep(15)
       print("--------  Mail sent successfully  ------------")
    except SMTPException as error:
        print ("\n\nSending mail is unsuccessful")
        print("****************reason****************\n")
        print(error)
        print("\n********************************")
#-------------------------------------------------------------------

now = datetime.datetime.now()
classtime = now.replace(hour=20, minute=2, second=0, microsecond=0)


wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'Yaswanth') 
sheet1.write(1, 0, 'Harika') 
sheet1.write(2, 0, 'Narsimha') 
sheet1.write(3, 0, 'Bharat Babu')

att1 = 0
att2 = 0
att3 = 0
att4 = 0
#---------------------------------------------------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('im',im)
        qwe= recognizer.predict(gray[y:y+h,x:x+w])
        print(qwe)
        ty="unkown"
        if(qwe[0] == 1 ):
            
            if(qwe[1] <= 100):
                print ("Yaswanth")
                ty="Yaswanth"
                time.sleep(0.2)
                now = datetime.datetime.now()
                if(now < classtime):
                    att1 = 1
            else:
                print ("unknown")
                ty="unknown"
        elif(qwe[0] == 2 ):
            
            if(qwe[1] <= 100):                
                print ("Harika")
                ty="Harika"
                time.sleep(0.2)
                now = datetime.datetime.now()
                if(now < classtime):
                    att2 = 1
            else:               
                print ("unknown")
                ty="unknown"
                time.sleep(0.2)
                
        elif(qwe[0] == 3 ):
            
            if(qwe[1] <= 100):                
                print ("Narsimha")
                ty="Narsimha"
                time.sleep(0.2)
                now = datetime.datetime.now()
                if(now < classtime):
                    att3 = 1
            else:               
                print ("unknown")
                ty="unknown"
                time.sleep(0.2)
                
        elif(qwe[0] == 4 ):
            
            if(qwe[1] <= 100):                
                print ("Bharath")
                ty="Bharath"
                time.sleep(0.2)
                now = datetime.datetime.now()
                if(now < classtime):
                    att4 = 1
            else:               
                print ("unknown")
                ty="unknown"
                time.sleep(0.2)
 #--------------------------------------------------------------------            
        elif(qwe[0] == 5 ):
            
            if(qwe[1] <= 100):                
                print ("unknown")
                ty="unknown"
                time.sleep(0.2)
            else:               
                print ("unknown")
                ty="unknown"
                time.sleep(0.2)
#----------------------------------------------------------------------     

        cv2.putText(im, str(ty), (x,y-40), font, 2, (255,0,0), 1)
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()

if(att1 == 1):
    sheet1.write(0, 1,'PRESENT')
else:
    sheet1.write(0, 1,'ABSENT')

if(att2 == 1):
    sheet1.write(1, 1,'PRESENT')
else:
    sheet1.write(1, 1,'ABSENT')
    
if(att3 == 1):
    sheet1.write(2, 1,'PRESENT')
else:
    sheet1.write(2, 1,'ABSENT')
    
if(att4 == 1):
    sheet1.write(3, 1,'PRESENT')
else:
    sheet1.write(3, 1,'ABSENT')

wb.save('xlwt example.xls') 
print("excel file saved...")

cv2.destroyAllWindows()
send_an_email()
cv2.destroyAllWindows()

