#!/usr/bin/env python

f = open('input.txt','r')
data = f.readline().strip()
f.close()

print 'Read in %d characters' % len(data)

floor = 0
count = 0
basement = None
for f in data:
    if f == '(':
        floor += 1
        count += 1
    elif f == ')':
        floor -= 1
        count += 1
    else:
        print 'Unknown input character: %s' % f

    if floor < 0 and basement is None:
        basement = count
        
print 'Floor is: %d' % floor
print 'Basement entered at input: %d' % basement

