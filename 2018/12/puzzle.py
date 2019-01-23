#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

init = data[0].split()[2].strip()
data = data[2:]
data = [line.strip() for line in data]

SLOP = 2000
pots = ''.join(['.'] * SLOP + list(init) + ['.'] * SLOP)

rules = {}
for line in data:
    rule, _, res = line.split()
    rules[rule] = res

print rules

def run_gen(pots, rules):
    new_pots = list(pots)
    for ii in xrange(2, len(pots)-1):
        state = ''.join(pots[ii-2:ii+3])
        if rules.has_key(state):
            new_pots[ii] = rules[state]
        else:
            new_pots[ii] = '.'

    return ''.join(new_pots)

def find_sum(offset, pots):
    sum = 0
    for ii in xrange(len(pots)):
        if pots[ii] == '#':
            #print ii - SLOP
            #sum += ii - SLOP
            sum += ii + offset
    return sum

sums = []
for gen in xrange(1,101):
    if pots[2] == '#' or pots[-3] == '#':
        print 'ERROR'
        sys.exit()

    new_pots = run_gen(pots, rules)
    pots = new_pots
    #print gen, ''.join(pots)
    
    sums.append(find_sum(-SLOP, pots))
    #print sums[-5:], sums[-1] * 5
    if len(sums) > 20 and (sums[-5:] == (sums[-1] * 5)):
        print 'Not growing', gen, sums[-1]
        sys.exit()

print find_sum(-SLOP, pots)
print sums
sys.exit()

def get_raw_state(pots):
    inds = [ii for ii, plant in enumerate(pots) if plant == '#']
    offset = inds[0]
    return (offset, ''.join(pots[inds[0]:inds[-1]+1]))

raw_states = {}
for gen in xrange(1,50000000000):
    if pots[2] == '#' or pots[-3] == '#':
        print 'ERROR'
        sys.exit()

    new_pots = run_gen(pots, rules)
    #print gen, ''.join(pots)
    
    sums.append(find_sum(pots))
    #print sums[-5:], sums[-1] * 5
    if len(sums) > 20 and (sums[-5:] == (sums[-1] * 5)):
        print 'Not growing', gen, sums[-1]
        sys.exit()

    #offset, raw = get_raw_state(pots)
    #if raw_states.has_key(raw):
    #    print 'cycle found'
    #    sys.exit()
    #raw_states[raw] = True
    if raw_states.has_key(''.join(pots)):
        print 'cycle', gen
        print pots
        print new_pots
        sys.exit()

    raw_states[''.join(pots)] = ''.join(new_pots)

    pots = new_pots
