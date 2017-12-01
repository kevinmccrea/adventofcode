#!/usr/bin/env python
import md5

f = open('input', 'r')
data = f.readline().strip()
f.close()

suffix = 0
answer5 = None
answer6 = None
while not answer5 or not answer6:
    key = data + str(suffix)
    if not answer5 and md5.md5(key).hexdigest().startswith('00000'):
        answer5 = suffix
    
    if not answer6 and md5.md5(key).hexdigest().startswith('000000'):
        answer6 = suffix
    
    suffix += 1

print 'suffix for 5 zeros: %s' % str(answer5)
print 'suffix for 6 zeros: %s' % str(answer6)
    
