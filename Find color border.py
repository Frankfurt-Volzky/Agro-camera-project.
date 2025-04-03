'''
BGR to HSV Color Conversion
    Create by Henry Dang ==> See the tutorial here:
    https://henrydangprg.com/2016/06/26/color-detection-in-python-with-opencv/
Adapted by Marcelo Rovai - MJRoBot.org @8Feb18
'''

import sys
import numpy as np
import cv2
def color_border():
    blue = int(input())
    green = int(input())
    red = int(input())  
    
    color = np.uint8([[[blue, green, red]]])
    print('color = ',color)
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    print('hsv_color = ',hsv_color)
    hue = hsv_color[0][0][0]
    hue2 = hsv_color[0][0][1]
    hue3 = hsv_color[0][0][2]
    #hue2 = hsv_color[1][0][0]
    #hu3 = hsv_color[2][0][0]
    print('hue =',hue)
    #print('hue2 =',hue2)
    #print('hue3 =',hue3)
    print("Lower bound is :"),
    print("[" + str(hue-10) + ",",hue2-10,',',hue3-10,"]")
    
    print("Upper bound is :"),
    print("[" + str(hue + 10) + ",",hue2+10,',',hue3+10,"]")
color_border()