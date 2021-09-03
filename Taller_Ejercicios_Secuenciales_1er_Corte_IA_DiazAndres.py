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

# 4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.

print('\n-------------- DATOS PARA AHORROS BANCARIOS --------------\n')
saldo_inicial = float(input('Digite el saldo inicial del cliente: '))
saldo_final = saldo_inicial * 1.015
print('----- RESUMEN DE DATOS DE AHORRO DEL CLIENTE -----\n')
print(f'Saldo inicial del cliente es: ${saldo_inicial:,}')
print(f'Saldo final del cliente es: ${saldo_final:,}')

# 5. Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# algoritmo que determine el monto de cada descuento y el monto total
# a pagar al trabajador.

print('-------------- DESCUENTOS SALARIALES --------------\n')
salario = float(input('Digite el salario del trabajador: '))
des_politica_pub = salario * 0.01
des_seg_social = salario * 0.04
des_seg_forzoso = salario * 0.005
des_caja_ahorro = salario * 0.05
des_total = des_politica_pub+des_seg_social+des_seg_forzoso+des_caja_ahorro
total_devengado = salario - des_total

print('\n----- Resumen salarial de descuentos del trabajador -----\n')
print('----- Salario base -----\n')
print(f'Salario del trabajador: ${salario:,}\n')
print('------ Descuentos ------\n')
print(f'Politica pública (1.0%): ${des_politica_pub:,}')
print(f'Seguro social    (4.0%): ${des_seg_social:,}')
print(f'Seguro forzoso   (0.5%): ${des_seg_forzoso:,}')
print(f'Caja de ahorro   (5.0%): ${des_caja_ahorro:,}')
print(f'Total descuentos       : ${des_total:,}\n')
print('-------------------------------------------')
print(f'Total devengado con descuento  : ${total_devengado:,}\n')

# 6. El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.

print('\n-------------- DATOS INICIALES DE LA COTIZACIÓN --------------\n')
num_palabras = int(input('Digite número de palabras: '))
tamanio = float(input('Digite tamaño en centimetros: '))
num_colores = int(input('Digite número de colores: '))
costo_num_palabras = num_palabras * 20000
costo_tamanio = tamanio * 15000
costo_num_colores = num_colores * 25000
costo_total = costo_num_palabras + costo_tamanio + costo_num_colores

print('\n-------------- PERIODICO EL INFORMADOR --------------\n')
print('-------------- Resumen de cotización de aviso --------------\n')
print(f'Costo de {num_palabras} palabras es:   ${costo_num_palabras:,}\n')
print(f'Costo de {tamanio} cm es:         ${costo_tamanio:,}\n')
print(f'Costo de {num_colores} colores es:     ${costo_num_colores:,}\n')
print('-------------------------------------------')
print(f'Costo total de la cotización: ${costo_total:,}\n')



















