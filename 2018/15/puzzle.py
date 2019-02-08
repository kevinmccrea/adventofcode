#!/usr/bin/env python

import sys
import collections
import itertools
import aoc
import copy

debug = False

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

base_map = {}
for rr in xrange(len(data)):
    line = data[rr]
    for cc in xrange(len(line)):
        base_map[(rr,cc)] = line[cc]

class Character:
    def __init__(self, pos, type, health=0, attack=0):
        self.pos = pos
        self.type = type
        self.health = health
        self.attack = attack
    def __str__(self):
        return '<%s %s A%d H%d>' % (self.type, self.pos, self.attack, self.health)
    def __repr__(self):
        return self.__str__()

goblins = []
elves = []
for k, v in base_map.items():
    if v == 'G':
        goblins.append(Character(k, 'G', 200, 3))
        base_map[k] = '.'
    if v == 'E':
        elves.append(Character(k, 'E', 200, 3))
        base_map[k] = '.'

# directions (in reading order)
DIRS = ((-1,0), (0,-1), (0,1), (1, 0))
WALLS = '#EG'

MAP_ROWS = len(data)
MAP_COLS = len(data[0])

def add_characters(base_map, characters):
    """
    Adds characters to a base map
    """
    combined = dict(base_map)
    for char in characters:
        if char.health > 0:
            combined[char.pos] = char.type
    return combined

def find_move_target_positions(player_map, players, start):
    """
    Returns a list of all of the possible (unobstructed) movement target 
    locations
    """
    targets = []
    for char in players:
        # character is dead
        if char.health <= 0:
            continue        

        # character is me
        if char.pos == start:
            continue

        for step in DIRS:
            target = aoc.tup_add(char.pos, step)
            if player_map[target] not in WALLS:
                targets.append(target)

    return targets

def get_target_position(player_map, player, targets):
    """
    Takes a list of move target positions and figures out which is 
    the closest.  Ties are done in reading order.
    """
    targets.sort()
    target = None
    min_dist = 0
    for pos in targets:
        route = aoc.astar_route(player_map, player.pos, pos, DIRS, WALLS)
        if route:
            dist = len(route)
            if not target or dist < min_dist:                
                target = pos
                min_dist = dist

    return target

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
            if tt.health <= 0:
                continue

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
        test_pos = aoc.tup_add(player.pos, step)

        if player_map[test_pos] in WALLS:
            continue
    
        if test_pos == goal:
            new_pos = test_pos
            break

        route = aoc.astar_route(player_map, test_pos, goal, DIRS, WALLS)
        if route:
            num_steps = len(route)
            if not min_steps or num_steps < min_steps:
                new_pos = test_pos
                min_steps = num_steps

    return new_pos

def all_dead(units):
    for unit in units:
        if unit.health > 0:
           return False
    return True

def any_dead(units):
    for unit in units:
        if unit.health <= 0:
            return True
    return False

def draw_map(player_map, all_units, rows, cols):
    for rr in xrange(rows):
        line = ''
        for cc in xrange(cols):
            line += player_map[(rr,cc)]

        line += '  '
        row_units = sorted([uu for uu in all_units if uu.pos[0] == rr], key=lambda t: t.pos)
        for unit in row_units:
            line += ' %s(%d)' % (unit.type, unit.health)

        print line

def compute_outcome(rounds, all_units):
    hp = 0
    for unit in all_units:
        if unit.health > 0:
            hp += unit.health
    return hp * rounds

def run_combat(base_map, elves, goblins):
    
    round = 0
    done = False
    while not done:
        # sort into reading order
        all_units = elves + goblins
        all_units.sort(key=lambda t: t.pos)

        for unit in all_units:

            # skip dead units
            if unit.health <= 0:
                continue
            
            # redraw the current map
            player_map = add_characters(base_map, all_units)

            if unit.type == 'E':
                enemy_list = goblins
            else:
                enemy_list = elves

            #
            # Move
            #
            if not get_adjacent_target(unit.pos, enemy_list):
                move_targets = find_move_target_positions(player_map, enemy_list, unit.pos)
                if move_targets:
                    target_loc = get_target_position(player_map, unit, move_targets)
                    if target_loc:
                        new_pos = get_next_step(player_map, unit, target_loc)
                        if new_pos:
                            unit.pos = new_pos
                            #player_map = add_characters(base_map, all_units)

            #
            # Attack
            #
            target = get_adjacent_target(unit.pos, enemy_list)
            if target:
                target.health -= unit.attack

            # check for end
            if all_dead(enemy_list):
                done = True
                break

        
        if not (all_dead(elves) or all_dead(goblins)):
            round += 1

        if debug:
            print 'Round %d' % round
            draw_map(player_map, all_units, MAP_ROWS, MAP_COLS)

    return (round, all_units)

orig_elves = copy.deepcopy(elves)
orig_goblins = copy.deepcopy(goblins)

round, units = run_combat(base_map, elves, goblins)
print 'Part one:', compute_outcome(round, units)

def find_win_point(base_map, orig_elves, orig_goblins):
    done = False
    curr = 4
    lo = None
    hi = None
    while not done:
        
        elves = copy.deepcopy(orig_elves)
        goblins = copy.deepcopy(orig_goblins)
        
        for ee in elves:
            ee.attack = curr

        print 'Running at %d' % curr
        round, units = run_combat(base_map, elves, goblins)
        outcome = compute_outcome(round, units)
        print 'outcome', outcome

        if all_dead(goblins) and not any_dead(elves):
            print 'Elves win at %d' % curr
            win_outcome = outcome
            hi = curr
        else:
            print 'Elves lose at %d' % curr
            lo = curr

        if hi == None:
            curr *= 2
        elif lo == None:
            curr /= 2
        else:
            curr = (hi + lo) / 2

        print 'hi', hi, 'lo', lo, 'curr', curr
        if hi == lo + 1:
            done = True

    return win_outcome

outcome = find_win_point(base_map, orig_elves, orig_goblins)
print 'Part 2', outcome
