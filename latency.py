# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.


from __future__ import division
speed_of_light = 300000. # km per second

def speed_fraction(traceroute_time, distancekm):

        #50 ms to travel 5000km,
        km_per_ms  =   distancekm/traceroute_time
        print km_per_ms
        km_per_second = km_per_ms *1000
        print km_per_second
        fraction_of_c = km_per_second/speed_of_light
        print  fraction_of_c       
        fraction_of_c = fraction_of_c * 2 # assuming round trip 
        return fraction_of_c

        



print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?
print speed_fraction(16,20)
#0.00833333333333` 
