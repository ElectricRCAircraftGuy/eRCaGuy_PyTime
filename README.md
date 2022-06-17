# PyTiming


## Description:    
Create some low-level Arduino-like millis() & delay() (for milliseconds) and micros() and delayMicroseconds() (for microseconds) timing functions for Python.

Compatible with Python in both Windows *and* Linux. Has ultra-great resolution timestamps (sub-microsecond), even in older versions of Python 3 which don't natively support (in the [time](https://docs.python.org/2.7/library/time.html) module, for instance) high resolutions like this.  


## Author:  
Gabriel Staples    
www.ElectricRCAircraftGuy.com  
-click "Contact me" at the top of my website to find my email address  


## Website:   
http://www.electricrcaircraftguy.com/2016/07/arduino-like-millisecond-and-microsecond-timestamps-in-python.html


## My other timing libraries and code:
1. For anyone looking for a **precision timing library on Linux in C or C++**, see my library here. It is one of my best works yet, as of June 2022:
    1. [timinglib.h](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib.h)
    1. [timinglib.c](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib.c)
    1. Demos:
        1. [timinglib_get_resolution.c](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib_get_resolution.c)
        1. [timinglib_pthread_periodic_loop.c](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib_pthread_periodic_loop.c)
        1. [timinglib_sleep_and_sleep_until.c](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib_sleep_and_sleep_until.c)
        1. [timinglib_timestamps_basic.c](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib_timestamps_basic.c)
        1. [timinglib_timestamps_rapid.c](https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/c/timinglib_timestamps_rapid.c)
1. My 3 sets of timestamp functions (cross-linked to each other):
    1. For **C timestamps**, see my answer here: [Get a timestamp in C in microseconds?](https://stackoverflow.com/a/67731965/4561887)
    1. For **C++ high-resolution timestamps**, see my answer here: [Here is how to get simple C-like millisecond, microsecond, and nanosecond timestamps in C++](https://stackoverflow.com/a/49066369/4561887)
    1. For **Python high-resolution timestamps**, see my answer here: [How can I get millisecond and microsecond-resolution timestamps in Python?](https://stackoverflow.com/a/38319607/4561887)


## History:  
(newest on top)
 * 20160907 - v0.2.1 created - updated delay functions to use modulus operator to guarantee proper C uint32_t-like underflow subtraction behavior when the timer rolls over  
 * 20160813 - v0.2.0 created - added Linux capability  
 * 20160711 - v0.1.0 created - functions for Windows *only* (via the QPC timer) 

