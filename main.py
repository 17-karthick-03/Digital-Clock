from machine import Pin, I2C
import time
from ws2812 import WS2812
from ds1307 import DS1307
import network
import socket
import umail

X=255
Y=0
Z=0
LIGHT = WS2812(Pin(16),30)
#AM_PM = WS2812(Pin(14),2)

RTC = I2C(1,scl = Pin(3),sda = Pin(2),freq = 100000)

def CLOCK(x,y,z):
    
    X=x
    Y=y
    Z=z
    #GET REALTIME FROM RTC MODULE
    DS = DS1307(RTC)
    TIME = DS.datetime()
    
    HOURS = TIME[4]
    MINUTES = TIME[5]
    
    #CONVERT 24 hr to 12 hr FORMAT
    if HOURS < 13:
        HOUR = HOURS
    else:
        HOUR = HOURS % 12
    #CONFIGURE TIMING TO GLOW THE LIGHT
    H_2 = HOUR % 10
    H_1 = HOUR // 10
    M_1 = MINUTES // 10
    M_2 = MINUTES % 10
    print(H_1,H_2,M_1,M_2)
    
    LIGHT[14]=LIGHT[15]=[x,y,z]
    LIGHT.write()
    time.sleep(0.8)
    LIGHT[14]=LIGHT[15]=[0,0,0]
    LIGHT.write()
    
                                  #DIGIT------1
    if H_1 == 0 or H_1 != 1: 
        for i in range(7):
            LIGHT[i]=[x,y,z]
        LIGHT[3]=[0,0,0]
        LIGHT.write()
    elif H_1 == 1:
        for i in range(7):
            LIGHT[i]=[0,0,0]
        LIGHT[2]=LIGHT[6]=[x,y,z]
        LIGHT.write()
                                #DIGIT--------2
    if H_2 == 0:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[10]=[0,0,0]
        LIGHT.write()
    elif H_2 == 1:
        for i in range(7,14):
            LIGHT[i]=[0,0,0]
        LIGHT[9]=LIGHT[13]=[x,y,z]
        LIGHT.write()
    elif H_2 ==2:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[7]=LIGHT[13]=[0,0,0]
        LIGHT.write()
    elif H_2 == 3:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[7]=LIGHT[11]=[0,0,0]
        LIGHT.write()
    elif H_2 == 4:
        for i in range(7,14):
            LIGHT[i]=[0,0,0]
        LIGHT[7]=LIGHT[9]=LIGHT[10]=LIGHT[13]=[x,y,z]
        LIGHT.write()
    elif H_2 == 5:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[9]=LIGHT[11]=[0,0,0]
        LIGHT.write()
    elif H_2 == 6:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[9]=[0,0,0]
        LIGHT.write()
    elif H_2 == 7:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[7]=LIGHT[10]=LIGHT[11]=LIGHT[12]=[0,0,0]
        LIGHT.write()
    elif H_2 == 8:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT.write()
    elif H_2 == 9:
        for i in range(7,14):
            LIGHT[i]=[x,y,z]
        LIGHT[11]=[0,0,0]
        LIGHT.write()
    
                       #DIGIT--------3
        
    if M_1 == 0:
        for i in range(16,23):
            LIGHT[i]=[x,y,z]
        LIGHT[19]=[0,0,0]
        LIGHT.write()
    elif M_1 == 1:
        for i in range(16,23):
            LIGHT[i]=[0,0,0]
        LIGHT[18]=LIGHT[22]=[x,y,z]
        LIGHT.write()
    elif M_1 ==2:
        for i in range(16,23):
            LIGHT[i]=[x,y,z]
        LIGHT[16]=LIGHT[22]=[0,0,0]
        LIGHT.write()
    elif M_1 == 3:
        for i in range(16,23):
            LIGHT[i]=[x,y,z]
        LIGHT[16]=LIGHT[20]=[0,0,0]
        LIGHT.write()
    elif M_1 == 4:
        for i in range(16,23):
            LIGHT[i]=[0,0,0]
        LIGHT[16]=LIGHT[18]=LIGHT[19]=LIGHT[22]=[x,y,z]
        LIGHT.write()
    elif M_1 == 5:
        for i in range(16,23):
            LIGHT[i]=[x,y,z]
        LIGHT[18]=LIGHT[20]=[0,0,0]
        LIGHT.write()
        
                 #DIGIT----------4
    if M_2 == 0:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[26]=[0,0,0]
        LIGHT.write()
    elif M_2 == 1:
        for i in range(23,30):
            LIGHT[i]=[0,0,0]
        LIGHT[25]=LIGHT[29]=[x,y,z]
        LIGHT.write()
    elif M_2 ==2:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[23]=LIGHT[29]=[0,0,0]
        LIGHT.write()
    elif M_2 == 3:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[27]=LIGHT[23]=[0,0,0]
        LIGHT.write()
    elif M_2 == 4:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[24]=LIGHT[27]=LIGHT[28]=[0,0,0]
        LIGHT.write()
    elif M_2 == 5:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[25]=LIGHT[27]=[0,0,0]
        LIGHT.write()
    elif M_2 == 6:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[25]=[0,0,0]
        LIGHT.write()
    elif M_2 == 7:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[26]=LIGHT[27]=LIGHT[28]=LIGHT[23]=[0,0,0]
        LIGHT.write()
    elif M_2 == 8:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT.write()
    elif M_2 == 9:
        for i in range(23,30):
            LIGHT[i]=[x,y,z]
        LIGHT[27]=[0,0,0]
        LIGHT.write()
    time.sleep(0.8)
    
while True:
    CLOCK(34,230,230)
