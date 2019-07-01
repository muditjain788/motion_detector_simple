#!/usr/bin/python3

import cv2
#starting camera 
cap=cv2.VideoCapture(0)
#[1] is passed beacuse cap.read() gives to things first is status which we don;t what that is 0th element and second is image [1]
tp1=cap.read()[1] # take 1
tp2=cap.read()[1]
tp3=cap.read()[1]

#now creating image differentiator
def img_diff(x,y,z):
  #diff b/w x and y that is tp1 and tp2 --d1
  #diff b/w y and z that is  tp2 and tp3 --d2
  #absolute diff b/w d1 and d2
  d1=cv2.absdiff(x,y)
  d2=cv2.absdiff(y,z)
  finalimg=cv2.bitwise_and(d1,d2)
  return finalimg

#now apply function
while cap.isOpened():
  status,frame=cap.read() #combine image folder
  motionimg=img_diff(tp1,tp2,tp3)
  #replacing image frame
  tp1=tp2
  tp2=tp3
  tp3=frame#passing live image to tp3
  cv2.imshow('live',frame)
  cv2.imshow('motion',motionimg)
  if  cv2.waitKey(10) & 0xff == ord('q') :
    break
cv2.destroyAllWindows()
cap.release()
