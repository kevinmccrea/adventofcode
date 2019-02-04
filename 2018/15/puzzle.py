#!/usr/bin/env python

import sys
import collections
import itertools
import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

maze = {}
for rr in xrange(len(data)):
    line = data[rr]
    for cc in xrange(len(line)):
        maze[(rr,cc)] = line[cc]

class Character:
    def __init__(self, pos, type, health=0, attack=0):
        self.pos = pos
        self.type = type
        self.health = health
        self.attack = attack

goblins = []
elves = []
for k, v in maze.items():
    if v == 'G':
        goblins.append(Character(k, 'G', 200, 3))
        maze[k] = '.'
    if v == 'E':
        elves.append(Character(k, 'E', 200, 3))
        maze[k] = '.'

# directions (in reading order)
DIRS = ((-1,0), (0,-1), (0,1), (1, 0))
WALLS = '#EG'

def add_characters(base_map, characters):
    """
    Adds characters to a base map
    """
    combined = dict(base_map)
    for char in characters:
        combined[char.pos] = char.type
    return combined

def find_move_targets(player_map, players, start):
    """
    Returns a list of all of the possible (unobstructed) movement target 
    locations
    """
    targets = []
    for char in players:
        if char.pos == start:
            continue

        for step in DIRS:
            target = aoc.tup_add(char.pos, step)
            if player_map[target] not in WALLS:
                targets.append(target)

    return targets

def get_adjacent_target(pos, targets):
    """
    Check all targets in target list for a target that is exactly
    one step away from pos and has the lowest hit points. 
    Returns the target or None if nothing is adjacent
    """
    # DIRS are in reading order so targets will be returned correctly
    if not targets:
        return None
        
    target = None
    for step in DIRS:
        test_pos = aoc.tup_add(pos, step)
        for tt in targets:
            if tt.pos == test_pos:
                if target == None or (tt.health < target.health and tt.health > 0):
                    target = tt
    
    return target

def get_next_step(player_map, player, goal):
    """
    Returns the next step that a unit should take.  Checks
    all first steps from player in reading order to 
    break ties.  Returns none if no step should be taken
    """
    min_steps = None
    new_pos = None
    for step in DIRS:
        test_pos = tup_add(player.pos, step)

        if player_map[test_pos] in WALLS:
            continue

        num_steps = len(astar_route(player_map, test_pos, goal, DIRS, WALLS))
        if not min_steps or num_steps < min_steps:
            new_pos = test_pos

    return new_pos

def run_combat():
    
    round = 0
    done = False
    while not done:
        all_units = elves + goblins
        all_unites.sort(key=lambda t: t.pos)



start = (1,2)
end = (3,4)
prevs, costs = aoc.astar(maze, start, end, DIRS, WALLS)
print prevs
print costs

route = aoc.path_route(prevs, costs, start, end)
print route
print len(route)
