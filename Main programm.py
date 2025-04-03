
import numpy as np
y1 = 750
y2 = 1000
xx = 0
a = []
percl = []
def color_border():
    blue = int(input())
    green = int(input())
    red = int(input())
    
    color = np.uint8([[[blue, green, red]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    hue = hsv_color[0][0][0]
    print("Lower bound is:")
    print("[" + str(hue-10)+", 100, 100]\n")
    print("Upper bound is:")
    print("[" + str(hue+10)+", 255, 255]")
    return hue



photo = cv2.imread("111.jpg",1)
photo = cv2.resize(photo, (1000,1000), fx=0.2, fy=0.2)
hsv = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV)
 
hue = color_border()
lower_range = np.array([hue-20, 100, 0], dtype= np.uint8)
upper_range = np.array([hue+20,255,100], dtype= np.uint8)
mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask',mask)
cv2.imshow('photo',photo)
for i in range(4):
    x = str(i)
    curt_p= mask[y1:y2,0:1000]
    cv2.imshow('urt_p'+x,curt_p)
    y1-=250
    y2-=250
    a.append(curt_p)
for i in a:
    every_pixel = 0
    needed_pixel = 0
    for u in i:
        for u1 in u:
            if u1 == 0:every_pixel+=1
            elif u1 != 0:needed_pixel+=1;#print(u);print(i)
    print(every_pixel)
    print(needed_pixel)
    percent = needed_pixel/every_pixel*100
    print(percent)
    xx+=1
    percl.append(xx)
    percl.append(percent)
    

    
print(a)
cv2.imshow('urt_p4'+x,a[0])
print(percl)

cv2.waitKey(0)
cv2.destroyAllWindows()
print('konec')
