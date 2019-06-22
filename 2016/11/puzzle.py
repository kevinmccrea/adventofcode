#!/usr/bin/env python

import sys
import itertools
import operator
import copy

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

# SG SM PG PM TG TM RG RM CG CM   E
#  1  1  1  1  2  3  2  2  2  2   1

#start_state = (1, [1, 1, 1, 1, 2, 3, 2, 2, 2, 2], [], None)
start_state = (1, [2, 1, 3, 1], [], None)

# state: (ele, curr_state, prev_states, next_states)
def calc_next_moves(state):
    moves = []

    # append all the one moves
    poss_inds = [ii for ii in xrange(len(state[1])) if state[1][ii] == state[0]]
    #print 'poss: ', poss_inds
    #for ii in xrange(len(state[1])):
    for ii in poss_inds:
        moves.append([1 if ii == yy else 0 for yy in xrange(len(state[1]))])

    # append combinations
    for comb in itertools.combinations(poss_inds,2):
        moves.append([1 if ii in comb else 0 for ii in xrange(len(state[1]))])

    #print moves
    return moves

def is_valid(state):
    valid = True
    if any(ii > 4 or ii < 1 for ii in state[1]):
        #print 'out'
        return False
    for chip_ind in xrange(1, len(state[1]), 2):
        if state[1][chip_ind - 1] != state[1][chip_ind]:
            for gen_ind in xrange(0, len(state[1]), 2):
                if state[1][gen_ind] == state[1][chip_ind]:
                    #print 'chip:', chip_ind, 'gen:', gen_ind
                    valid = False
    return valid

def is_done(state):
    return all(state[1][ii] == 4 for ii in xrange(len(state[1])))

# state: (ele, curr_state, prev_states, next_states)
#def run_state(ele, curr_state, prev_states):
wins = []
STATES = {}
def run_state(state):
    #print 'State:', state
    #raw_input('')
    ele = state[0]
    curr_state = copy.deepcopy(state[1])
    prev_states = copy.deepcopy(state[2])
    #print 'enter', len(prev_states)
    if is_valid(state) and is_done(state):
        print 'WIN: ', state, len(prev_states)
        wins.append(copy.deepcopy(state))
        return

    if STATES.has_key(str(curr_state)):
        if len(STATES[str(curr_state)]) <= len(prev_states):
            print 'SHORTCUT', curr_state
            return
    
    STATES[str(curr_state)] = copy.deepcopy(prev_states)

    moves = calc_next_moves(state)
    if moves:
        if ele < 4:
            for move in moves:
                new_state = map(operator.add, copy.deepcopy(curr_state), move)
                #print 'new_state:', new_state
                #print 'prev_states:', prev_states
                #print new_state in prev_states
                if new_state not in prev_states and is_valid((ele+1, new_state, [],[])):
                    #print 'running'
                    run_state((ele+1, new_state, prev_states + [curr_state]))

        if ele > 1:
            for move in moves:
                new_state = map(operator.sub, copy.deepcopy(curr_state), move)
                if new_state not in prev_states and is_valid((ele-1, new_state, [], [])):
                    run_state((ele-1, new_state, prev_states + [curr_state]))

    #print 'BACK TRACK'

#sys.setrecursionlimit(500)
run_state(start_state)

print wins

#print is_valid((2,[3, 2, 3, 1], [], []))
#print is_valid((3,[3, 3, 3, 1], [], []))
#print is_valid((3,[3, 2, 2, 2], [],[] ))


