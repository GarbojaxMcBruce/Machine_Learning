# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:56:58 2017

@author: Garbojax
"""

import pickle
import Operations as op
import Environment as env
import Hunter as hnt
import Creature as crt

creature = pickle.load(open('trained_creature.sav', 'rb'))
creature.value_function = pickle.load(open('brain.sav', 'rb'))
hunter = hnt.Hunter('demo_hunter', -1000)
environment = env.Environment('Demo', 10, creature, hunter)

op.interactive_trial(environment)

