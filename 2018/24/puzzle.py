#!/usr/bin/env python

import sys
import collections
import itertools
import re
import copy

import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

regex_attr = re.compile(r"(?P<units>\d+) units each with (?P<hit_points>\d+) hit points (?P<attribs>\(.*\)) with an attack that does (?P<attack>\d+) (?P<attack_type>\S+) damage at initiative (?P<initiative>\d+)")
regex_noattr = re.compile(r"(?P<units>\d+) units each with (?P<hit_points>\d+) hit points with an attack that does (?P<attack>\d+) (?P<attack_type>\S+) damage at initiative (?P<initiative>\d+)")

def build_group(descrip, army_index, army_name, group_index):
    group = dict(descrip)

    group['army_index'] = army_index
    group['army_name'] = army_name
    group['group_index'] = group_index

    # convert types
    group['units'] = int(group['units'])
    group['hit_points'] = int(group['hit_points'])
    group['attack'] = int(group['attack'])
    group['initiative'] = int(group['initiative'])

    # expand the attribs
    group['weak'] = []
    group['immune'] = []
    if group['attribs']:
        attribs = group['attribs'][1:-1]
        for attr in attribs.split(';'):
            tokens = attr.split(',')
            type = tokens[0].split()[0].strip()
            values = [t.split()[-1].strip() for t in tokens]
            group[type] = values

    return group

def other_army(index):
    return (index + 1) % 2

def eff_power(group):
    return group['units'] * group['attack']

def all_dead(army):
    for group in army:
        if group['units'] > 0:
            return False
    return True

def compute_attack(attacker, defender):
    attack = eff_power(attacker)
    attack_type = attacker['attack_type']

    if attack_type in defender['weak']:
        attack *= 2
    if attack_type in defender['immune']:
        attack = 0

    return attack

def sum_units(army):
    sum = 0
    for group in army:
        if group['units'] > 0:
            sum += group['units']
    return sum

armies = [[],[]]
current_army = 0
current_name = 'Immune'
current_index = 1
for line in data[1:]:
    if not line or 'Immune System:' in line:
        continue

    if 'Infection:' in line:
        current_army = 1
        current_name = 'Infection'
        current_index = 1
        continue

    if '(' in line:
        tokens = re.search(regex_attr, line).groupdict()
    else:
        tokens = re.search(regex_noattr, line).groupdict()
        tokens['attribs'] = None

    armies[current_army].append(build_group(tokens, current_army, current_name, current_index))
    current_index += 1

def print_armies(armies):
    print 'Immune System:'
    groups = sorted(armies[0], key=lambda t: t['group_index'])
    for g in groups:
        print 'Group %d contains %d units' % (g['group_index'], g['units'])
    print 'Infection:'
    groups = sorted(armies[1], key=lambda t: t['group_index'])
    for g in groups:
        print 'Group %d contains %d units' % (g['group_index'], g['units'])
    print ''

def run_combat(armies):
    done = False
    while not done:
        all_groups = list(armies[0] + armies[1])
        battles = []
        
        #print_armies(armies)

        #
        # target selections
        #
        attackers = list(all_groups)
        attackers.sort(key=lambda t: t['initiative'], reverse=True)
        attackers.sort(key=lambda t: eff_power(t), reverse=True)
        defenders = list(attackers)

        for attacker in attackers:
            if attacker['units'] <= 0:
                continue

            #print attacker
            defender = None
            max_attack = 0
            for dd in defenders:
                if dd['units'] <= 0:
                    continue

                if dd['army_index'] == attacker['army_index']:
                    continue

                attack = compute_attack(attacker, dd)
                if attack > max_attack:
                    max_attack = attack
                    defender = dd

                #print '%s group %d would deal defending group %d %d damage' % (attacker['army_name'], 
                #                                                               attacker['group_index'],
                #                                                               dd['group_index'],
                #                                                               attack)                

            if defender:
                battles.append((attacker, defender))
                defenders.remove(defender)

        #
        # Fight Phase
        #

        # sort battles by initiative
        battles.sort(key=lambda t: t[0]['initiative'], reverse=True)

        total_killed = 0
        for attacker, defender in battles:
            if attacker['units'] <= 0:
                continue

            attack = compute_attack(attacker, defender)
            units_killed = int(attack / defender['hit_points'])

            defender['units'] -= units_killed
            total_killed += units_killed
            #print '%s group %d attacks defending group %d killing %d units' % (attacker['army_name'], attacker['group_index'], defender['group_index'], units_killed)

        #
        # Check for winner
        #
        if all_dead(armies[0]) or all_dead(armies[1]) or (total_killed == 0):
            done = True


orig_armies = copy.deepcopy(armies)

run_combat(armies)

if all_dead(armies[0]):
    print 'Infection wins', sum_units(armies[1])

if all_dead(armies[1]):
    print 'Immune wins', sum_units(armies[0])

def wrapper(armies, boost):

    for group in armies[0]:
        group['attack'] += boost

    run_combat(armies)

    if all_dead(armies[1]):
        return sum_units(armies[0])
    else:
        return None

result = aoc.minimize_variable(wrapper, orig_armies, 1, debug=True)
print 'Part 2:', result
