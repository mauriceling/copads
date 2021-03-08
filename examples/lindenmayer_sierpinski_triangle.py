import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))

import random
from lindenmayer import lindenmayer

axiom = 'A'
rules = [['A', 'BLALB'],
         ['B', 'ARBRA']]
start_position = (-300, 250)
iterations = 8
turtle_file = '19_lindenmayer_sierpinski_turtle.py'
image_file = '19_lindenmayer_sierpinski_turtle.svg'
mapping = {'set_angle': 60,
           'random_angle': 0,
           'set_distance': 2.5,
           'random_distance': 0,
           'background_colour': 'RoyalBlue1',
           'A': 'forward',
           'B': 'forward',
           'R': 'right',
           'L': 'left'}

l = lindenmayer(1)
l.add_rules(rules)
l.generate(axiom, iterations)
l.turtle_generate(turtle_file, image_file, start_position, mapping)
