"""
sleep_test.py
-see what the resolution of the time.sleep() function is 
By Gabriel Staples
http://www.ElectricRCAircraftGuy.com 
-click "Contact me" at the top of my website to find my email address 

13 Aug. 2016 
"""

import time
import GS_timing as timing

def delayMicroseconds(n):
    time.sleep(n / 1000000.)

def delayMillisecond(n):
    time.sleep(n / 1000.)

t_start = 0
t_end = 0

#using time.sleep
print('using time.sleep')
print('delayMicroseconds(1)')
for x in range(10):
    t_start = timing.micros() #us 
    delayMicroseconds(1)
    t_end = timing.micros() #us
    print('dt (us) = ' + str(t_end - t_start))
print('delayMicroseconds(2000)')
for x in range(10):
    t_start = timing.micros() #us 
    delayMicroseconds(2000)
    t_end = timing.micros() #us
    print('dt (us) = ' + str(t_end - t_start))
  
#using GS_timing
print('\nusing GS_timing')
print('timing.delayMicroseconds(1)')
for x in range(10):
    t_start = timing.micros() #us 
    timing.delayMicroseconds(1)
    t_end = timing.micros() #us
    print('dt (us) = ' + str(t_end - t_start))
print('timing.delayMicroseconds(2000)')
for x in range(10):
    t_start = timing.micros() #us 
    timing.delayMicroseconds(2000)
    t_end = timing.micros() #us
    print('dt (us) = ' + str(t_end - t_start))
    
"""
SAMPLE RESULTS ON MY WINDOWS 8.1 MACHINE:

using time.sleep
delayMicroseconds(1)
dt (us) = 2872.059814453125
dt (us) = 886.3939208984375
dt (us) = 770.4649658203125
dt (us) = 1138.7698974609375
dt (us) = 1426.027099609375
dt (us) = 734.557861328125
dt (us) = 10617.233642578125
dt (us) = 9594.90576171875
dt (us) = 9155.299560546875
dt (us) = 9520.526611328125
delayMicroseconds(2000)
dt (us) = 8799.3056640625
dt (us) = 9609.2685546875
dt (us) = 9679.5439453125
dt (us) = 9248.145263671875
dt (us) = 9389.721923828125
dt (us) = 9637.994262695312
dt (us) = 9616.450073242188
dt (us) = 9592.853881835938
dt (us) = 9465.639892578125
dt (us) = 7650.276611328125

using GS_timing
timing.delayMicroseconds(1)
dt (us) = 53.3477783203125
dt (us) = 36.93310546875
dt (us) = 36.9329833984375
dt (us) = 34.8812255859375
dt (us) = 35.3941650390625
dt (us) = 40.010986328125
dt (us) = 38.4720458984375
dt (us) = 56.425537109375
dt (us) = 35.9072265625
dt (us) = 36.420166015625
timing.delayMicroseconds(2000)
dt (us) = 2039.526611328125
dt (us) = 2046.195068359375
dt (us) = 2033.8841552734375
dt (us) = 2037.4747314453125
dt (us) = 2032.34521484375
dt (us) = 2086.2059326171875
dt (us) = 2035.4229736328125
dt (us) = 2051.32470703125
dt (us) = 2040.03955078125
dt (us) = 2027.215576171875


SAMPLE RESULTS ON MY RASPBERRY PI VERSION 1 B+:

using time.sleep
delayMicroseconds(1)
dt (us) = 1022.0
dt (us) = 417.0
dt (us) = 407.0
dt (us) = 450.0
dt (us) = 2078.0
dt (us) = 393.0
dt (us) = 1297.0
dt (us) = 878.0
dt (us) = 1135.0
dt (us) = 2896.0
delayMicroseconds(2000)
dt (us) = 2746.0
dt (us) = 2568.0
dt (us) = 2512.0
dt (us) = 2423.0
dt (us) = 2454.0
dt (us) = 2608.0
dt (us) = 2518.0
dt (us) = 2569.0
dt (us) = 2548.0
dt (us) = 2496.0

using GS_timing
timing.delayMicroseconds(1)
dt (us) = 572.0
dt (us) = 673.0
dt (us) = 1084.0
dt (us) = 561.0
dt (us) = 728.0
dt (us) = 576.0
dt (us) = 556.0
dt (us) = 584.0
dt (us) = 576.0
dt (us) = 578.0
timing.delayMicroseconds(2000)
dt (us) = 2741.0
dt (us) = 2466.0
dt (us) = 2522.0
dt (us) = 2810.0
dt (us) = 2589.0
dt (us) = 2681.0
dt (us) = 2546.0
dt (us) = 3090.0
dt (us) = 2600.0
dt (us) = 2400.0


"""
