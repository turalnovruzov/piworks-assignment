"""
This file is not used  to solve the given problem.
It only generates random input configurations.

Usage: python generate.py file_name depth max_value
"""

import sys
import random

def generate(depth, max_value):
    result = ''
    # Loop through the depth
    for d in range(1, depth + 1):
        line = ''
        # Print random numbers current depth times
        for _ in range(d):
            line += f'{random.randint(1, max_value)} '
        
        # Append the line to the result
        result += line + '\n'
    
    return result

filename, depth, max_value = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

with open(filename, 'w') as f:
    content = generate(depth, max_value)
    f.write(content)
