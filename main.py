"""
    Execute the function for get the radius circumference.

    1. Require import the calculator file.
"""

import calculator

if __name__ == '__main__':
    radius = int(input('Escriba el radio de la circunferencia: '))
    result = calculator.print_circum(radius)
    print(f'El diametro es: {result}')
