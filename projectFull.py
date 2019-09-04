from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
import random
import os
import datetime
import ctypes
import pymysql
import mysql.connector
ctypes.windll.kernel32.SetConsoleTitleW("ID CARD Generator by HarDarSHEL")
db=pymysql.connect("localhost","root","","ostproj")
cursor=db.cursor()
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print ('_______________________________________________________________________________________________________________________\n')
print (reg_format_date)
print ('_______________________________________________________________________________________________________________________')
print('\n\nAll Fields are Mandatory') 
print('Write Everything in uppercase letters')
(x,y) = (350, 50)
comp = input('\nEnter Your Company Name: ')
company=comp
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype("arial.ttf", 40, encoding="unic")
draw.text((x,y), comp, fill=color, font=font)
(x,y) = (430, 100)
idno=random.randint(10000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
draw.text((x,y), message, fill=color, font=font)
(x,y) = (50, 250)
fname = input('Enter Your Name and Surname: ')
name=fname
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
draw.text((x, y), fname, fill=color, font=font)
(x, y) = (50, 350)
ge = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)'
draw.text((x, y), ge, fill=color, font=font)
(x,y) = (250,350)
a = input('Enter Your Age: ')
color = 'rgb(0, 0, 0)'
draw.text((x,y), a, fill=color, font=font)
(x,y) = (50,450)
dateofb = input('Enter Your Date Of Birth(dd-mm-yy): ')
color = 'rgb(0, 0, 0)'
draw.text((x,y), dateofb, fill=color, font=font)
(x,y) = (50,550)
bg = input('Enter Your Blood Group: ')
color = 'rgb(255, 0, 0)'
draw.text((x,y), bg, fill=color, font=font)
(x,y) = (50,650)
m = input('Enter Your Mobile Number: ')
temp=m
color = 'rgb(0, 0, 0)'
draw.text((x,y), m, fill=color, font=font)
(x,y) = (50,750)
addr = input('Enter Your State and City: ')
color = 'rgb(0, 0, 0)'
draw.text((x,y), addr, fill=color, font=font)
try:
    cursor.execute("INSERT INTO `ost`(`COMPANY`, `FULL NAME`, `GENDER`, `AGE`, `DOB`, `BLOOD GROUP`, `PHONE`, `ADDRESS`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (comp,name,ge,a,dateofb,bg,temp,addr))
    db.commit()
except:
    print('DATABASE ERROR!!!!')
    db.rollback()
db.close() 
image.save(str(name)+'.png')
import qrcode
img = qrcode.make(str(company)+str(idno))
img.save(str(idno)+'.bmp')
from PIL import Image
til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp')
til.paste(im,(690,600))
til.save(name+'.png')
import cv2
img = cv2.imread(name+'.png')
color = [0,255,255]
top, bottom, left, right = [30]*4
img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
lineThickness = 2
cv2.line(img_with_border,(0, 220), (1060, 220), (0,0,0),  lineThickness)
cv2.imwrite(name+'.png',img_with_border)
print ('SMILE! TAKING YOUR IMAGE SWITCH TO CAMERA WINDOW PRESS "s" TO CLICK')
camera = cv2.VideoCapture(0)
def change_res(width, height):
    camera.set(3, width)
    camera.set(4, height)
change_res(354,472)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
til = Image.open(name+'.png')
im = Image.open('test.jpg')
til.paste(im,(650,300))
til.save(name+'.png')
cv2.destroyAllWindows()
print('\n\n\nYour ID Is Successfully created in a PNG file '+name+'.png')
input('\n\nPress any key to Close program...')
