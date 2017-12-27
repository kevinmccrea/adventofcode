#!/usr/bin/env python

import sys
import collections

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

def deref(regs, val):
    try:
        ret = int(val)
        return ret
    except:
        return int(regs[val])

regs = collections.defaultdict(int)

pc = 0
num_mults = 0
#regs['a'] = 1
while pc >= 0 and pc < len(data):
    ops = data[pc].split()
    #print ops

    offset = 1

    op = ops[0]
    #if op == 'snd':
    #    freq = deref(regs, ops[1])
    if op == 'set':
        regs[ops[1]] = deref(regs, ops[2])
    elif op == 'add':
        regs[ops[1]] += deref(regs, ops[2])
    elif op == 'sub':
        regs[ops[1]] -= deref(regs, ops[2])
    elif op == 'mul':
        regs[ops[1]] *= deref(regs, ops[2])
        num_mults += 1
    elif op == 'mod':
        regs[ops[1]] %= deref(regs, ops[2])
    #elif op == 'rcv':
    #    if deref(regs, ops[1]) != 0:
    #        rec_freq = freq
    #        print rec_freq
    #        break
    elif op == 'jnz':
        if deref(regs, ops[1]) != 0:
            offset = deref(regs, ops[2])

    elif op == 'jgz':
        if deref(regs, ops[1]) > 0:
            offset = deref(regs, ops[2])
    else:
        print 'ERROR'
        break

    pc += offset

    #print regs['h']
    #print ops, regs

print "Part 1: %d" % num_mults
print regs['h']

class proc:
    def __init__(self, id, send_queue, recv_queue):
        self.id = id
        self.pc = 0
        self.regs = collections.defaultdict(int)
        self.regs['p'] = id
        self.send_queue = send_queue
        self.recv_queue = recv_queue
        self.num_sends = 0
        self.blocked = False
        self.done = False

    def step(self, code):
        ops = code[self.pc].split()
        #print ops
        
        if self.pc < 0 or self.pc >= len(code):
            self.done = True
            return

        offset = 1

        op = ops[0]
        if op == 'snd':
            val = deref(self.regs, ops[1])
            self.send_queue.append(val)
            #print "proc %d sending %d" % (self.id, val)
            self.num_sends += 1
        elif op == 'set':
            self.regs[ops[1]] = deref(self.regs, ops[2])
        elif op == 'add':
            self.regs[ops[1]] += deref(self.regs, ops[2])
        elif op == 'mul':
            self.regs[ops[1]] *= deref(self.regs, ops[2])
        elif op == 'mod':
            self.regs[ops[1]] %= deref(self.regs, ops[2])
        elif op == 'rcv':
            if len(self.recv_queue) > 0:
                self.blocked = False
                val = self.recv_queue.pop(0)
                self.regs[ops[1]] = val
                #print "proc %d recv %d" % (self.id, val)
            else:
                offset = 0
                self.blocked = True

        elif op == 'jgz':
            if deref(self.regs, ops[1]) > 0:
                offset = deref(self.regs, ops[2])
        else:
            print 'ERROR'

        self.pc += offset

queues = [[],[]]
procs = [proc(0, queues[1], queues[0]), proc(1, queues[0], queues[1])]

curr_proc = 0
while (not procs[0].done or not procs[1].done) and not (procs[0].blocked and procs[1].blocked):
    procs[curr_proc].step(data)
    curr_proc = (curr_proc + 1) % len(procs)


print "Part 2: %d" % procs[1].num_sends


