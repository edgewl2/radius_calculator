"""
    Execute the function for get the radius circumference.

    1. Require import the calculator file.
"""

import calculator

if __name__ == '__main__':
    diameter = int(input('Escriba el diametro de la circunferencia: '))
    result = calculator.print_circum(diameter)
    print(f'El radio es: {result}')
