#!/usr/bin/env python

import re

f = open('input.txt', 'r')
data = f.readlines()
f.close()

num_nice = 0
for line in data:
    naughty = False
    if not len(re.findall(r'[aeiou]', line)) >= 3:
        naughty = True

    if not re.findall(r'(.)\1', line):
        naughty = True

    if re.findall(r'ab|cd|pq|xy', line):
        naughty = True

    if not naughty:
        num_nice += 1

print 'Num nice: %d' % num_nice

num_nice = 0
for line in data:
    naughty = False
    if not re.findall(r'(..).*\1', line):
        naughty = True

    if not re.findall(r'(.).\1', line):
        naughty = True

    if not naughty:
        num_nice += 1

print 'Num nice: %d' % num_nice
