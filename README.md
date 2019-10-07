# CircuitPython
These are my CircuitPython assigments that I have done.

## Hello CircuitPython
### Description 
In this assignment, I used the new metro boards along with the new language, Circuitpython. I used this to make an LED fade from on to of.

### Lessons Learned
This assignment was a bit tough becuase it was our first experience with Circuitpython, Metro, and Mu. I had to google a lot of stuff, such as how to set up a pin for a LED and how to make it fade. The syntax between Circuitpython and the arduino language is very different, meaning there is not really any crossover. We had to essentially learn how to do things all over again. 

### Pictures
This is a quick Fritzing of this assignment. As you can see, it is very simple to wire. 
![Fritzing for LED_Fade](/H:/Pictures/LED_Fade_Fritzing_bb.png)

## Servo with Capacitive Touch
### Description
In this assignment, I used two wires to control a servo. Touching one wire turned the servo towards 0, while touching the other wire turned the servo towards 180. 

### Lessons Learned
This assignment was hard because it was the first time I used a PWM pin. The setup is different from analog and gital pins, so we had to do a bit of research to figure out how to set it up. Also, we used capacitive touch for the first time. This enabled us to control the servo without having any buttons. 

### Pictures

## LCD With Button
### Description
In this assignment, I used an LCD screen, button, and a switch. The objective was to be able to display the number of times a button was pressed on the LCD screen. The switch was there to switch the direction of the counting. For example, one state would count up, and the other would count down. 

### Lessons Learned
We used a button and a switch for the first time in this assignment. Like everything else, we had to look up how to use buttons and switches. In the end the code wasn't very hard. We did have a bit of issues with the timing. Sometimes, the LCD would count twice, and sometimes it would count at all. We had to mess around with the delays a bit and find the right timing. 

### Pictures

## Photointerrupter
### Description
In this assignment, we used a photointerruper and displayed the number of interruptions every 4 seconds. In addition, we were not allowed to use time.sleep(). Instead, we had to use time.monotonic(). 

### Lessons Learned
In this assignment, we learned how to use time.monotonic(). It essentially counts the number of seconds and then prints every 4 seconds. This way we can still count the number of interruptions every second but only print them every 4 seconds. 

### Pictures

## Distance Sensor
### Description
For this assignment, we only used an ultrasonic sensor. We had to get distances from the sensor, and then display a color on the onboard LED that corrosponded with the distance. 

### Lessons Learned
We were using ultrasonic sensors for the first time with circuitpython, so we learned how to do that. Also, we learned how to map values in circuitpython, which proved to be very important for this assignment. 

### Pictures

## Classes, Objects, and Modules
### Description
In this assignment, we learned how to do classes, objects, and modules in circuitpython. We had to create a library that enabled us to use the code given to us. The code given was suppossed to manipulate RGB LEDs by turnign them on, switching colors, and then fading them through the colors of the rainbow. 

### Lessons Learned
We learned how to map values in circuitpython, which was important because we had to convert many values. We also learned how to use and wire RGB LEDs. Overall, this assignment was fairly challenging. 

### Pictures

## Hello VS Code
### Description
In this assignment, we had to print "Hello" in Visual Studio code. 

### Lessons Learned
Although this assignment may seem very simple, it was hard because it was our first time using VS code. There weere a lot of errors and bugs that we had to go through and fix. To some extent, this carried over to the next assignment because we were still running into some of the same issues.

### Pictures

## FancyLED
### Description
In this assignment, we had to wire 6 LEDs and then create a library that was able to use the code given to us. 

### Lessons Learned
During this assignment, we learned how to better use different things in VS code such as serial monitor and terminal. In some ways, this assignment was similar to the Classes, Objects, and Modules assignment because we were using the same sort of structure. 

### Pictures

