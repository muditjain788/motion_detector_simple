#!/usr/bin/python3

import cv2
#starting camera 
cap=cv2.VideoCapture(0)
tp1=cap.read()[1] # take 1
tp2=cap.read()[1]
tp3=cap.read()[1]
#to make pic more perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

#now creating image differentiator
def img_diff(x,y,z):
  #diff b/w x and y that is gray1 and gray2  --d1
  #diff b/w y and z that is gray2 aand gray3 --d2
  #absolute diff b/w d1 and d2
  d1=cv2.absdiff(x,y)
  d2=cv2.absdiff(y,z)
  finalimg=cv2.bitwise_and(d1,d2)
  return finalimg

#now apply function
while cap.isOpened():
  status,frame=cap.read() #combine image folder
  motionimg=img_diff(gray1,gray2,gray3)
  #replacing image frame
  gray1=gray2
  gray2=gray3
  gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #passing live image to gray3
  cv2.imshow('live',frame)
  cv2.imshow('motion',motionimg)
  if  cv2.waitKey(10) & 0xff == ord('q') :
    break


cv2.destroyAllWindows()
cap.release()
