# PyTiming
## Description:    
Create some low-level Arduino-like millis() & delay() (for milliseconds) and micros() and delayMicroseconds() (for microseconds) timing functions for Python.

Compatible with Python in both Windows *and* Linux. Has ultra-great resolution timestamps (sub-microsecond), even in older versions of Python 3 which don't natively support (in the [time](https://docs.python.org/2.7/library/time.html) module, for instance) high resolutions like this.  

## Website:   
http://www.electricrcaircraftguy.com/2016/07/arduino-like-millisecond-and-microsecond-timestamps-in-python.html

## History:  
(newest on top)
 * 20160907 - v0.2.1 created - updated delay functions to use modulus operator to guarantee proper C uint32_t-like underflow subtraction behavior when the timer rolls over  
 * 20160813 - v0.2.0 created - added Linux capability  
 * 20160711 - v0.1.0 created - functions for Windows *only* (via the QPC timer) 
 
## Author:  
Gabriel Staples    
www.ElectricRCAircraftGuy.com  
-click "Contact me" at the top of my website to find my email address  
