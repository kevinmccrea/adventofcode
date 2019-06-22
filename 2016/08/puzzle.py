#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

screen = [[0 for cc in xrange(50)] for rr in xrange(6)]
#screen = [[0 for cc in xrange(7)] for rr in xrange(3)]

def print_screen(screen):
    for rr in xrange(len(screen)):
        for cc in xrange(len(screen[rr])):
            if screen[rr][cc]:
                print '#',
            else:
                print ' ',
            #print screen[rr][cc],
        print ''

for line in data:
    line = line.strip()

    if line.find('rect') >= 0:
        (x, y) = line.split()[1].split('x')

        for rr in xrange(int(y)):
            for cc in xrange(int(x)):
                screen[rr][cc] = 1

        print_screen(screen)

    elif line.find('rotate row') >= 0:
        (row_index, trash, iters) = line.split('=')[1].split(' ')
        print line, ' ', row_index, ' ', iters

        row = screen[int(row_index)]
        for ii in xrange(int(iters)):
            row = row[-1:] + row[:-1]
        screen[int(row_index)] = row

        print_screen(screen)
    elif line.find('rotate column') >= 0:
        (col_index, trash, iters) = line.split('=')[1].split(' ')
        
        col = [screen[rr][int(col_index)] for rr in xrange(len(screen))]
        for ii in xrange(int(iters)):
            col = col[-1:] + col[:-1]
        for rr in xrange(len(col)):
            screen[rr][int(col_index)] = col[rr]
        
        print_screen(screen)

    else:
        print 'oops'

num = 0
for rr in xrange(len(screen)):
    for cc in xrange(len(screen[rr])):
        if screen[rr][cc]:
            num += 1

print
print_screen(screen)
print num

