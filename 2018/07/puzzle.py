#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

deps = {}
all_nodes = set()
for line in data:
    dep = line.split()[1]
    target = line.split()[7]
    if not deps.has_key(target):
        deps[target] = []
    deps[target].append(dep)

    all_nodes.add(dep)
    all_nodes.add(target)

roots = all_nodes - set(deps.keys())
for key in roots:
    deps[key] = []

deps_backup = {}
for key, val in deps.items():
    deps_backup[key] = list(val)

completed = ''
while len(deps.keys()):
    ready = sorted([t for t in deps.keys() if len(deps[t]) == 0])
    
    if not len(ready):
        print 'ERROR'
        sys.exit()

    run = ready[0]
    
    for key,val in deps.items():
        if val.count(run):
            val.remove(run)
            
    completed += run
    del deps[run]

print completed

deps = {}
for key, val in deps_backup.items():
    deps[key] = list(val)

completed = ''
workers = [0] * 5
jobs = [None] * 5
time = 0
while len(deps.keys()):
    
    print '###############3 ITERATION '
    # complete jobs
    for ww in xrange(len(workers)):
        if workers[ww] == 0 and jobs[ww]:
            job = jobs[ww]
            for key,val in deps.items():
                if val.count(job):
                    val.remove(job)
                    
            print 'Job complete', job, 'worker', ww
            completed += job
            jobs[ww] = None


    # assign jobs
    ready = sorted([t for t in deps.keys() if len(deps[t]) == 0])
    for rr in xrange(len(ready)):
        for ww in xrange(len(workers)):
            if jobs[ww] == None:
                run = ready[rr]
                jobs[ww] = run
                workers[ww] = 60 + ord(run) - ord('A') + 1
                print run
                del deps[run]
                break

    # tic time
    time += 1
    for ww in xrange(len(workers)):
        if workers[ww] > 0:
            workers[ww] -= 1

    print time, workers, jobs, completed
    print deps

    #if time > 70:
    #    sys.exit()
            
print time
print workers
print time + max(workers)
    
