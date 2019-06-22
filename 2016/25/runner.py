import os
import sys

a = 0
try:
    while True:
        print 'Running %d' % a
        os.system('./puzzle.py %d' % a)
        a += 1
except:
    sys.exit()

