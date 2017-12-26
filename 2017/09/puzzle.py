#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = data[0].strip()

#data = '{{{},{},{{}}}}'
#data = '{{<!>},{<!>},{<!>},{<a>}}'
ii = 0

is_garbage = False
total_groups = 0
group_stack = 0
group_score = 0
garbage_count = 0

while ii < len(data):
    ch = data[ii]

    if ch == '!':
        if is_garbage:
            ii += 2
            continue

    if ch == '{':
        if not is_garbage:
            group_stack += 1
        else:
            garbage_count += 1
    elif ch == '}':
        if not is_garbage:
            group_score += group_stack

            group_stack -= 1
            total_groups += 1

            if group_stack < 0:
                print 'Error: ended group when not in group'
        else:
            garbage_count += 1
    elif ch == '<':
        if not is_garbage:
            is_garbage = True
        else:
            garbage_count += 1
    elif ch == '>':
        if is_garbage:
            is_garbage = False
    else:
        if is_garbage:
            garbage_count += 1


    ii += 1

print 'Part 1: score %d' % group_score
print 'Part 2: garbage count %d' % garbage_count

