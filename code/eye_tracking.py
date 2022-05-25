# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 07:15:01 2021

@author: arabtech
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2
class eyetrackingcode :
   
  
   def takepic (self,picpath):
      self.img=cv2.imread(picpath,0)
      while True :
         cv2.imshow('image',self.img,)
         if cv2.waitKey(20) & 0xff == 27 :
            break
      cv2.destroyAllWindows()
      return  self.img
   
   def filteration (self,image):
      self.blur=image
      self.blur = cv2.GaussianBlur(image,(5,5),10)
      while True :
         cv2.imshow('image blur',self.blur)
         if cv2.waitKey(20) & 0xff == 27 :
            break
      cv2.destroyAllWindows()
      return self.blur
   def dectectedgs (self,image):
      self.edges=image
      self.edges = cv2.Canny(image,60,90)
      while True :
         cv2.imshow('image canny',self.edges)
         if cv2.waitKey(20) & 0xff == 27 :
            break
      cv2.destroyAllWindows()
      return self.edges
   def thershold (self,image) :
      #adaptive mean threshold 
      self.AMT = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
      #adaptive Gaussian threshold 
      self.AGT = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
      #binary threshold
      ret,B_Thresh= cv2.threshold(image,10,70,cv2.THRESH_BINARY)
      return self.AMT
   
   def getpuiple(self,imgthre,imgedge) : 
      self.k= self.edges & self.AMT
      while True :
         cv2.imshow('canny & histequ',self.k)
         if cv2.waitKey(20) & 0xff == 27 :
           break
      cv2.imwrite('canny & histequ.png',self.k)
      cv2.destroyAllWindows()
      return self.k
   def getcountors (self,image) :
      #contours
      contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      #create an empty image for contours
      img_contours = np.zeros(image.shape)
      # draw the contours on the empty image
      cv2.drawContours(img_contours, contours, -1, (255,10,0), 3)
      max_area = -1
      #filtering countors by Area
      for i in range(len(contours)):
         area = cv2.contourArea(contours[i])
         if area>max_area:
                cnt = contours[i]
                max_area = area
      img_contours2 = np.zeros(image.shape)
      cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
      #ft elps and get center
      elps = cv2.fitEllipse(cnt)
      cv2.drawContours(self.img, cnt, -1, (255,0,100), 3)
      (x,y),radius = cv2.minEnclosingCircle(cnt)
      center = (int(x),int(y))
      cv2.circle(self.img, center, 3, (255, 255, 255), 1)

      while True :
         cv2.imshow('image contour with elips fit',self.img,)
         if cv2.waitKey(20) & 0xff == 27 :
            break
      cv2.imwrite('image contour with elips fit.png',self.img)
      cv2.destroyAllWindows()
      return image

start=eyetrackingcode()
k=start.takepic("mimir3.bmp")
l=start.filteration(k) 
e=start.dectectedgs(l)
m=start.getcountors(e)
