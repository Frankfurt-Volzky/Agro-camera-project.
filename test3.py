import cv2
import numpy as np
from time import sleep

def color_border():
    blue = int(input('blue'))
    green = int(input('green'))
    red = int(input('red'))  
    
    color = np.uint8([[[blue, green, red]]])
    
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    
    hue = hsv_color[0][0][0]
    
    print("Lower bound is :"),
    print("[" + str(hue-10) + ", 100, 100]\n")
    
    print("Upper bound is :"),
    print("[" + str(hue + 10) + ", 255, 255]")
    return hue

def split(image_name,width_cut,height_cut_max,height_cut_min):
  a = input('Хотите срезать изображение')
  if a == 'да':
   print('start doing spliting ')
   img = cv2.imread(image_name,1)
   width = img.shape[1]
   height = img.shape[0]
   print('Ширина = '+str(width),'Высота = '+str(height))
   try:
      cut = img[height_cut_min:height_cut_max,0:width]
      print('Срезывание прошло успешно')
      cv2.imshow('срез',cut)
      return cut
   except:
      print('Ваша длинна и ширина не валидна попробуйте другую')
      print(img[height_cut_min:height_cut_max,0:width])
      return image_name
    
    
  else:
    print('Не режем')
    return image_name

def fiding_color(image_name):
  m_w = int(input('длинна разреза'))
  max_h =int(input('Максимальная высота среза'))
  min_h = int(input('Минимальная выоста среза'))
  a = split(mask,m_w,max_h,min_h)
  every_pixel = 0
  needed_pixel = 0
  for i in a:
    for u in i:
      if u == 0:every_pixel+=1
      elif u != 0:needed_pixel+=1;#print(u);print(i)
  print(every_pixel)
  print(needed_pixel)
  percent = needed_pixel/every_pixel*100
  print(percent)
def mask_hsv(image_name):
  print('started hsv function')
  img = cv2.imread(image_name)
  img = cv2.resize(img, (1000,1000), fx=0.2, fy=0.2)
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
  hue = color_border()
  lower_range = np.array([hue-20, 90, 0], dtype=np.uint8) 
  upper_range = np.array([hue+20, 255, 90], dtype=np.uint8)
  mask = cv2.inRange(hsv, lower_range, upper_range)
  cv2.imshow('mask',mask)
  cv2.imshow('image', img)
  return mask
mask = mask_hsv("grass.jpeg")
sleep(1000)
fiding_color(mask)

# wait to user to press [ ESC ]
while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break
cv2.destroyAllWindows()