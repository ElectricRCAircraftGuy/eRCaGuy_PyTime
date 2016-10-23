"""
test.py
By Gabriel Staples
http://www.ElectricRCAircraftGuy.com 
-click "Contact me" at the top of my website to find my email address 

13 Aug. 2016 

"""

from GS_timing import *

print(micros())
print(millis())
print('version = ' + VERSION)

#SHOULD PRODUCE AN ERROR, since _constrain is module private
#-see here: http://stackoverflow.com/questions/1547145/defining-private-module-functions-in-python/1547160#1547160
print(_constrain(10,11,15)) #YEP! PRODUCES ERROR!