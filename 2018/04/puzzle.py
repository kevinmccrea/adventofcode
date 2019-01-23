#!/usr/bin/env python

import sys
import re
import numpy

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = sorted(data)

def add_sleep(guards, guard, start, end):
    if guard not in guards:
        guards[guard] = [0]* 60

    for min in xrange(start, end):
        guards[guard][min] += 1


on_duty = None
sleep_time = None
guards={}
for line in data:
    tokens = re.split(r"[\W']+", line)

    YYYY, MM, DD, hh, mm = map(int, tokens[1:6])

    if tokens[6] == 'Guard':
        if tokens[8] == 'begins':
            on_duty = tokens[7]
        else:
            print 'ERROR: ', tokens
            sys.exit(0)
    elif tokens[6] == 'falls':
        sleep_time = mm
    elif tokens[6] == 'wakes':
        wake_time = mm

        add_sleep(guards, on_duty, sleep_time, wake_time)
    else:
        'ERROR:', tokens


total_sleeps = {}
max_sleep = 0
max_guard = None

max_min_val = 0
max_min_min = None
max_min_guard = None

for guard, sleeps in guards.items():
    total = sum(sleeps)
    if total >= max_sleep:
        max_sleep = total
        max_guard = guard

    maxmin = numpy.argmax(sleeps)
    if sleeps[maxmin] > max_min_val:
        max_min_guard = guard
        max_min_min = maxmin
        max_min_val = sleeps[maxmin]

print max_guard
max_min = numpy.argmax(guards[max_guard])
print int(max_guard) * max_min


print int(max_min_guard) * max_min_min
