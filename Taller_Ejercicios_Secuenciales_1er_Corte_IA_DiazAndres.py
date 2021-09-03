# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:48:51 2021

@author: USER
"""

# Calcule el valor de Y indicando paso a paso como llegó al resultado

# 1. y=((5+2-5)^2*5+8/2-30)/2*5-3

y = ((5 + 2 - 5) ** 2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
print(f'El valor de y es: {y}')

# 2. z=5
# n=3
# m=z-n
# y=(((z+2-n)^2*m+8/2-30)/2*5-3)^5+15*3-9/3

z = 5
n = 3
m = z - n
y = (((z+2-n)**2*m+8/2-30)/2*5-3)**5+15*3-9/3
print(f'El valor de y es {y}')

# 3. z=5
# n=((8+2-4)^2*5+8+7/2-30*5)/2*5-3
# m= z^2*3+n
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4

z = 5
n = ((8+2-4)**2*5+8+7/2-30*5)/2*5-3
m = z**2*3+n
y = ((((z+2-n)**2*m+8/2-30)/2*5-3)**5+15*3-9/3)**2-5/4
print(f'El valor de y es {y}')

# Realizar los algoritmos que den solución a la problemática presentada
# en los siguientes ejercicios:

# 1. Haga un algoritmo que calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))

print('-------------- DATOS PARA EL CÁLCULO DE LA MASA --------------\n')
presion = float(input('Digite el valor de la presión: '))
volumen = float(input('Digite el valor del volúmen: '))
temperatura = float(input('Digite el valor de la temperatura: '))
masa = (presion*volumen)/(0.37*(temperatura+460))
print(f'El valor calculado de la masa es {masa}')

# 2. Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.

edad = int(input('Digite la edad de la persona: '))
num_pulsaciones = (200 - edad) / 10
print(f'El número de pulsaciones de la persona es: {num_pulsaciones}')


# 3. Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

print('\n------------- DATOS PARA EL REGISTRO DE INVERSIONES -------------\n')
inversion_persona1 = float(input('Digite la inversión de la 1ra persona: '))
inversion_persona2 = float(input('Digite la inversión de la 2da persona: '))
inversion_persona3 = float(input('Digite la inversión de la 3er persona: '))

total_inversion = inversion_persona1+inversion_persona2+inversion_persona3

porcentaje_persona1 = (inversion_persona1/total_inversion)*100
porcentaje_persona2 = (inversion_persona2/total_inversion)*100
porcentaje_persona3 = (inversion_persona3/total_inversion)*100

print('\n-------------- RESUMEN DE REGISTRO DE INVERSIONES --------------\n')
print('----- Datos primera persona -----')
print(f'Valor de la inversión: ${inversion_persona1:,}')
print(f'Porcentaje de participacion: {porcentaje_persona1}%\n')
print('----- Datos segunda persona -----')
print(f'Valor de la inversión: ${inversion_persona2:,}')
print(f'Porcentaje de participacion: {porcentaje_persona2}%\n')
print('----- Datos tercera persona -----')
print(f'Valor de la inversión: ${inversion_persona3:,}')
print(f'Porcentaje de participacion: {porcentaje_persona3}%')
























