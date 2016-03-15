import unicornhat as uni
import datetime
import Adafruit_CharLCD as LCD
import time

lcd = LCD.Adafruit_CharLCDPlate()
uni.brightness(0.1)

def showTime(time,col,r,g,b):
	binary = '{0:08b}'.format(time)
	for y in range(8):
		if binary[y] == '1':
			uni.set_pixel(col,y,r,g,b)
		else:
			uni.set_pixel(col,y,0,0,0)

while True:
	thetime = datetime.datetime.now()
	lcd.clear()
	lcd.message(thetime.strftime("%H:%M:%S"))

	showTime(thetime.second, 6, 255,0,0)
	showTime(thetime.minute, 5, 255,255,0)
	showTime(thetime.hour, 4, 0,255,255)	
	showTime(thetime.day, 3, 0,255,0)
	showTime(thetime.month, 2, 125, 125,0)


	uni.show()
	time.sleep(1)	

