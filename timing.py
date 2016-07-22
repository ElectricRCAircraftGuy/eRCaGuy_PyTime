#timing.py
#-create some low-level Arduino-like millis() (milliseconds) and micros() (microseconds) timing functions for Python 
#By Gabriel Staples
#http://www.ElectricRCAircraftGuy.com 
#-click "Contact me" at the top of my website to find my email address 
#Started: 11 July 2016 
#Updated: 11 July 2016 

"""
References:
-personal (C++ code): GS_PCArduino.h

1) Acquiring high-resolution time stamps (Windows)
   -https://msdn.microsoft.com/en-us/library/windows/desktop/dn553408(v=vs.85).aspx
2) QueryPerformanceCounter function (Windows)
   -https://msdn.microsoft.com/en-us/library/windows/desktop/ms644904(v=vs.85).aspx
3) QueryPerformanceFrequency function (Windows)
   -https://msdn.microsoft.com/en-us/library/windows/desktop/ms644905(v=vs.85).aspx
4) LARGE_INTEGER union (Windows)
   -https://msdn.microsoft.com/en-us/library/windows/desktop/aa383713(v=vs.85).aspx

-*****http://stackoverflow.com/questions/4430227/python-on-win32-how-to-get-absolute-timing-cpu-cycle-count
   
"""

from ctypes import *

#FUNCTIONS:

def micros():
    "return a timestamp in microseconds (us)"
    tics = c_int64()
    freq = c_int64()

    windll.Kernel32.QueryPerformanceCounter(byref(tics)) #get ticks on the internal ~2MHz QPC clock
    windll.Kernel32.QueryPerformanceFrequency(byref(freq)) #get the actual freq. of the internal ~2MHz QPC clock 
    
    t_us = tics.value*1e6/freq.value
    return t_us
    
def millis():
    "return a timestamp in milliseconds (ms)"
    tics = c_int64()
    freq = c_int64()

    windll.Kernel32.QueryPerformanceCounter(byref(tics)) #get ticks on the internal ~2MHz QPC clock
    windll.Kernel32.QueryPerformanceFrequency(byref(freq)) #get the actual freq. of the internal ~2MHz QPC clock 
    
    t_ms = tics.value*1e3/freq.value
    return t_ms

def delay(delay_ms):
    "delay for delay_ms milliseconds (ms)"
    tStart = millis()
    while (millis() - tStart < delay_ms):
      pass #do nothing 
    return

def delayMicroseconds(delay_us):
    "delay for delay_us microseconds (us)"
    tStart = micros()
    while (micros() - tStart < delay_us):
      pass #do nothing 
    return 

#EXAMPLES:
    
#print loop execution time 100 times, using micros()
tStart = micros() #us
for x in range(0, 100):
    tNow = micros() #us
    dt = tNow - tStart #us; delta time 
    tStart = tNow #us; update 
    print("dt(us) = " + str(dt))

#print loop execution time 100 times, using millis()
print("\n")
tStart = millis() #ms
for x in range(0, 100):
    tNow = millis() #ms
    dt = tNow - tStart #ms; delta time 
    tStart = tNow #ms; update 
    print("dt(ms) = " + str(dt))
    
#print a counter once per second, for 5 seconds, using delay 
print("\nstart")
for i in range(1,6):
    delay(1000)
    print(i)

#print a counter once per second, for 5 seconds, using delayMicroseconds
print("\nstart")
for i in range(1,6):
    delayMicroseconds(1000000)
    print(i)

    
    
