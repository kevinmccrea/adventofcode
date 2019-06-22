#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

class Bot:
    def __init__(self):
        self.values = []
        self.lo_bot = None
        self.hi_bot = None
        self._has_given = False
    def give(self, bots):
        self.values.sort()
        if not bots.has_key(self.lo_bot):
            bots[self.lo_bot] = Bot()
        bots[self.lo_bot].values.append(int(self.values[0]))

        if not bots.has_key(self.hi_bot):
            bots[self.hi_bot] = Bot()
        bots[self.hi_bot].values.append(int(self.values[1]))

        self._has_given = True

    def is_ready(self):
        if len(self.values) == 2:
            return True
        else:
            return False

    def has_given(self):
        return self._has_given

bot_map = {}

for line in data:
    line = line.strip()

    tokens = line.split()
    if line.startswith('value'):
        val = tokens[1]
        bot = tokens[4]+tokens[5]

        if not bot_map.has_key(bot):
            bot_map[bot] = Bot()

        bot_map[bot].values.append(int(val))

    elif line.startswith('bot'):
        src_bot = tokens[0]+tokens[1]
        lo_bot = tokens[5]+tokens[6]
        hi_bot = tokens[10]+tokens[11]

        if not bot_map.has_key(src_bot):
            bot_map[src_bot] = Bot()

        bot_map[src_bot].lo_bot = lo_bot
        bot_map[src_bot].hi_bot = hi_bot

    else:
        print 'fuck'



def num_not_given(bots):
    return [bot.has_given() for key,bot in bots.iteritems()].count(False)

def num_outputs(bots):
    outputs = []
    for key in bots.keys():
        print key
        if key.startswith('output'):
            outputs.append(key)
    return len(outputs)

print len(bot_map)
print num_outputs(bot_map)

outs = num_outputs(bot_map)
last_remaining = num_not_given(bot_map)
while num_not_given(bot_map)-num_outputs(bot_map) != 0:
    for key,bot in bot_map.copy().iteritems():
        if not bot.has_given() and bot.is_ready():
            bot.give(bot_map)

    if num_not_given(bot_map) - num_outputs(bot_map) == last_remaining:
        print 'STUCK'
        break

    last_remaining = num_not_given(bot_map) - num_outputs(bot_map)
    print 'remaining: ', num_not_given(bot_map)-num_outputs(bot_map)

for key,bot in bot_map.iteritems():
    bot.values.sort()
    if len(bot.values) == 2 and bot.values[0] == 17 and bot.values[1] == 61:
        print 'ans: ', key

print bot_map['output0'].values
print bot_map['output1'].values
print bot_map['output2'].values

print bot_map['output0'].values[0] * bot_map['output1'].values[0] * bot_map['output2'].values[0]


