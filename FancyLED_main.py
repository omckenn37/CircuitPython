from fancyLED import FancyLED #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error

# Sets the pins for both the LEDs
fancy1 = FancyLED(board.D2, board.D3, board.D4) 
fancy2 = FancyLED(board.D5, board.D6, board.D7)

while True:
    # This is all the functions that we had to use
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()
    
    
    