import cv2
import numpy as np
def split(image_name,width_cut,height_cut):
   print('start doing spliting ')
   img = cv2.imread(image_name,1)
   width = img.shape[1]
   height = img.shape[0]
   print('Ширина = '+str(width),'Высота = '+str(height))
   try:
      img = img[(height_cut//2):height,0:width]
      return img
   except:
      print('Ваша длинна и ширина не валидна попробуйте другую')
      return image_name
cv2.imshow('image', split('grass.jpeg'))
while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break
cv2.destroyAllWindows()   
    
    
