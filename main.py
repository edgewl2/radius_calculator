"""
    Execute the function for get the radius circumference.

    1. Require import the calculator file.
"""
import calculator

if __name__ == '__main__':
    __INPUT_COUNT__ = 3
    # __INPUT_COUNT__ = int(input('Escriba el numero calculos a hacer: '))
    if __INPUT_COUNT__ > 1:
        radius = [None] * __INPUT_COUNT__
        for iterator in range(__INPUT_COUNT__):
            radius[iterator] = int(input(f'Escriba el radio de la circunferencia {iterator + 1}: '))
        result = calculator.print_circum(radius)
        for item in result:
            print(f'El diametro {result.index(item) + 1} es: {item}')
    else:
        radius = int(input('Escriba el radio de la circunferencia: '))
        result = calculator.print_circum(radius)
        print(f'El diametro es: {result}')
