#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Denielle>
Student Number: <RWTDEN001>
Prac: <Prac 1>
Date: <22/07/2019>
"""
# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product 
# Logic that you write
"Configuring GPIO pins"
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)  "configuring led as an output pin"
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP) " configuring switch as pull up"
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
global count
count=0
disp =list( product ([0,1], repeat = 3)) "creating binary list "
print disp
def main():
	GPIO.setwarnings(False)
def button_increase(channel):
	global count
	count+=1  "incrementing led output when button is pushed"
	if count==8 : "when 8 is reached leds must loop back to 0"
                count=0
	GPIO.output(27,disp[count][0])
	GPIO.output(5,disp[count][1])
	GPIO.output(6,disp[count][2]) "leds displaying binary numbers"
GPIO.add_event_detect(26,GPIO.FALLING,callback=button_increase, bouncetime=100)
"event which calls the button_increase method when switch 1 is pressed"
def button_decrease(channel):
  	global count
	count-=1
 	if count==-1:
        	count=7
        GPIO.output(27,disp[count][0])
        GPIO.output(5,disp[count][1])
        GPIO.output(6,disp[count][2])
	print(count)
	print(disp[count][0], disp[count][1], disp[count][2])
GPIO.add_event_detect(17,GPIO.FALLING,callback=button_decrease, bouncetime=100)
"event which calls the button_decrease method when switch 2 is pressed"



# Only run the functions if
if __name__ == "__main__":
   # Make sure the GPIO is stopped correctly
    try:
      while True:
          main()
      GPIO.cleanup()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except :
        
        print("Some other error occurred")
        GPIO.cleanup()
