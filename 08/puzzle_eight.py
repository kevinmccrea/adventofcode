#!/usr/bin/env python

f = open('input', 'r')
strlen = 0
codelen = 0
encodedlen = 0
for line in f.readlines():

    strlen += len(eval(line.strip()))
    codelen += len(line.strip())

    encodedlen += len(line.strip().replace('\\', '\\\\').replace('"', '\\"')) + 2

print 'String len: %d' % strlen
print 'Code len: %d' % codelen
print 'Encoded len: %d' % encodedlen

print 'Diff: %d' % (codelen - strlen)
print 'Diff Encoded: %d' % (encodedlen - codelen)

f.close

