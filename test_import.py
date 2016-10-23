"""
test.py
By Gabriel Staples
http://www.ElectricRCAircraftGuy.com 
-click "Contact me" at the top of my website to find my email address 

13 Aug. 2016 

"""

import GS_timing as timing 

print(timing.micros())
print(timing.millis())
print('version = ' + timing.VERSION)

print(timing._constrain(10,11,15)) #11