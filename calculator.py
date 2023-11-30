"""
    This function receive an parameter integer type and use the form
    2πr when π = 3.14159 and r = parameter.
"""
import math

def print_circum(radius):
    if isinstance(radius, int):
        return round(2 * round(math.pi, 5) * radius, 2)
    else:
        radius_count = len(radius)
        if radius_count > 1:
            circum = [None] * radius_count
            for iterator in range(radius_count):
                value = 2 * round(math.pi, 5) * radius[iterator]
                circum[iterator] = round(value, 2)
            return circum