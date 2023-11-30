"""
    This function receive an parameter integer type and use the form
    2πr when π = 3.14159 and r = parameter.
"""
import math

def print_circum(radius):
    if isinstance(radius, int):
        return round(2 * round(math.pi, 5) * radius, 2)