#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

moves = data[0].strip().split(',')


def parse_move(move):
    step = move[0]
    args = move[1:].split('/')

    parsed = [step]
    parsed.extend(args)

    return tuple(parsed)

def spin(line, n):
    return line[-n:] + line[:-n]

def exchange(line, x, y):
    line = list(line)
    t = line[x]
    line[x] = line[y]
    line[y] = t
    return ''.join(line)

def partner(line, x, y):
    indx = line.index(x)
    indy = line.index(y)
    line = list(line)
    t = line[indx]
    line[indx] = line[indy]
    line[indy] = t
    return ''.join(line)

line = 'abcdefghijklmnop'

#moves = ['s1','x3/4','pe/b']
#line = 'abcde'

for move in moves:
    p = parse_move(move)
    #print str(p) + '    '  + line

    if (p[0] == 's'):
        line = spin(line, int(p[1]))
    elif (p[0] == 'x'):
        line = exchange(line, int(p[1]), int(p[2]))
    elif (p[0] == 'p'):
        line = partner(line, p[1], p[2])
    else:
        print 'yikes'
        sys.exit(0)

print line
orig_line = 'abcdefghijklmnop'

inds = [orig_line.index(c) for c in line]

print '$$$$$$$$$$$$$$$$$$$$'
print inds
print ''.join([orig_line[ind] for ind in inds])

print inds
#line = 'abcdefghijklmnop'
#line = list(line)
for ii in xrange(9):
    #ref_line = line
    for jj in xrange(9):
        line = ''.join([line[ind] for ind in inds])
        #print "###########################"
        #print line
        #line = [line[ind] for ind in inds]
    inds = [orig_line.index(c) for c in line]

    print inds
    print line


print ''.join(line)

print '#################'
history = []
line = orig_line
for ii in xrange(1000000000):
    moves = data[0].strip().split(',')

    for move in moves:
        p = parse_move(move)

        if (p[0] == 's'):
            line = spin(line, int(p[1]))
        elif (p[0] == 'x'):
            line = exchange(line, int(p[1]), int(p[2]))
        elif (p[0] == 'p'):
            line = partner(line, p[1], p[2])
        else:
            print 'yikes'
            sys.exit(0)

    if line in history:
        print "cycle at %d iterations" % len(history)
        print history
        print history[0], " ", line

        index = 1000000000 % len(history)
        print index
        print history[int(1000000000 % len(history))-1]

        break
    else:
        history.append(line)

print line
