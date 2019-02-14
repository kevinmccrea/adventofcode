#!/usr/bin/env python

ZERO = 0
ONE = 0
TWO = 0
THREE = 0
FOUR = 0
FIVE = 257

iters = 0
done = False
THREE = 0
FIVE = THREE | 65536
THREE = 15028787
prev = None
find_val = None
values = {}
while not done:
    TWO = FIVE & 255
    THREE = THREE + TWO
    THREE = THREE & 16777215
    THREE = THREE * 65899
    THREE = THREE & 16777215

    if FIVE < 256:
        TWO = 1
        iters += 1

        if values.has_key(THREE):
            done = True
        else:
            values[THREE] = True
            prev = THREE

        # set it the first time
        if not find_val:
            find_val = THREE

        TWO = 0
        FIVE = THREE | 65536
        THREE = 15028787

    else:
        if True:
            TWO = FIVE / 256
            FOUR = FIVE + (256 - (FIVE % 256))
            FIVE = TWO
        else:
            TWO = 0
            four_set = False
            loops = 0 
            #print 'BEFORE', TWO, FOUR, FIVE
            while not four_set:
                loops += 1
                FOUR = TWO + 1
                FOUR *= 256
                if FOUR > FIVE:
                    #FOUR = 1
                    four_set = True
                    FIVE = TWO
                else:
                    #FOUR = 0
                    TWO += 1
            #print 'AFTER', TWO, FOUR, FIVE, loops
        
    iters += 1

print 'Part 1:', find_val
print 'Part 2:', prev

