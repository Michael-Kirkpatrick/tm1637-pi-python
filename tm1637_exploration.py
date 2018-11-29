import tm1637_alt
import time
import RPi.GPIO as GPIO

# Simply change the CLK and DIO pin numbers of 23 and 24 to match the Pi GPIO pins you've used.
display = tm1637_alt.TM1637(CLK=23, DIO=24, brightness=2.0)
display.Clear()

display.ShowScroll(12345)
display.ShowScroll(123)
display.ShowScroll(12)
display.ShowScroll(1)
display.ShowScroll(1234567890)

display.Clear()
GPIO.cleanup()
