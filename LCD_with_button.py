# Owen McKenney
# LCD Screen
# This code displays the number of times you clicked a button on an LCD
# You can also toggle between counting up and down
 
# All the necessary libraries

# #pylint: disable-msg=import-error 
# is necessary to use libraries in VS code

import board #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error
import adafruit_bus_device #pylint: disable-msg=import-error

from lcd.lcd import LCD #pylint: disable-msg=import-error
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #pylint: disable-msg=import-error
from lcd.lcd import CursorMode #pylint: disable-msg=import-error

# Pin setup for the switch
inputPin = digitalio.DigitalInOut(board.D6)
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP

# Pin setup for the button
button = digitalio.DigitalInOut(board.D8)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16) # LCD screen setup

# All the variables used in this assignment
counter = 0
oldSwitchState = 0
newSwitchState = 1
adder = 1

while True:
    # Next few lines set up the LCD and print the initial message
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Button pressed: ")
    lcd.set_cursor_pos(1,0)
    lcd.print(str(counter))

    if button.value: # if the button value true
        print("0") 
        time.sleep(0.05)
        oldSwitchState = 0 # sets oldSwitchState to 0

    elif oldSwitchState == 0 and newSwitchState == 1: # if the oldSwitchState is 0 and the newSwitch state is 1
        if inputPin.value: # if the switch is flipped one direction, add
            adder = 1
        else: # if the switch is flipped the other direction, subtract
            adder = -1
        print("1")
        time.sleep(0.05)
        counter += adder 
        oldSwitchState = 1 