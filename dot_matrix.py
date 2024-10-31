'''
**********************************************************************
* Filename    : dot_matrix.py
* Description : Script show charactors and pictures on 8*8 led
*               dot matrix.
* Author      : Cavon and Anik
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-10-18    New release Anik 30-10-2024
**********************************************************************
'''

#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import tables

SDI   = 17
RCLK  = 18
SRCLK = 27

per_line = [0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]

def print_msg():
	print('Program is running...')
	print('Please press Ctrl+C to end the program...')

def setup():
	GPIO.setmode(GPIO.BCM)    # Number GPIOs by its BCM location
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

# Shift the data to 74HC595
def hc595_in(dat):
	for bit in range(0, 8):	
		GPIO.output(SDI, 1 & (dat >> bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.000001)
		GPIO.output(SRCLK, GPIO.LOW)

def hc595_out():
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.000001)
	GPIO.output(RCLK, GPIO.LOW)

def flash(table):
	for i in range(8):
		hc595_in(per_line[i])
		hc595_in(table[i])
		hc595_out()
	# Clean up last line
	hc595_in(per_line[7])
	hc595_in(0x00)
	hc595_out()

def show(table, second):
	start = time.time()
	while True:
		flash(table)
		finish = time.time()
		if finish - start > second:
			break

def main():
	flag = 0
	word_one = 'HAPPY'
	word_two = 'DIWALI'
	while True:
		for table in word_one:
			table = table.upper()
			if table == 'P' and flag == 0:
			    flag = 1
			if flag == 1:
     			    time.sleep(0.2)
			show(tables.charactors[table],1)

		print('smile')
		show(tables.picture['smile'],4)
		time.sleep(1)
		for table in word_two:
			show(tables.charactors[table],1)
		time.sleep(0.5)
		print('heart')
		show(tables.picture['heart'],4)
		time.sleep(1)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		main()
	except KeyboardInterrupt:
		destroy()
