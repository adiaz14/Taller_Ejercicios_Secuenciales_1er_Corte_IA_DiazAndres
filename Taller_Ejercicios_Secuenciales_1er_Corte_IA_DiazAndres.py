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

# 7. Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un algoritmo que determine el monto del bono
# a pagar a un trabajador que tiene varios años en la empresa.

print('---------- DATOS PARA LA LIQUIDACIÓN DE BONO LABORAL ----------\n')
antiguedad = int(input('Digite antigüedad (mayor a 0 años): '))
bono = (100000) + (120000 * (antiguedad - 1))

print('\n-------------- RESUMEN DE BONO DEL TRABAJADOR --------------\n')

print(f'Debido al servicio de {antiguedad} años, al trabajador se le otorga '
      f'un bono por: ${bono:,}\n')

# 8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.

print('\n-------------- DATOS DE LA JORNADA DEL PROFESOR --------------\n')
horas = float(input('Digite horas trabajadas por el profesor: '))
salario_bruto = horas * 20000
descuento = salario_bruto * 0.05
salario_neto = salario_bruto - descuento

print('\n-------------- RESUMEN SALARIAL DEL TRABAJADOR --------------\n')

print(f'El salario bruto del profesor por {horas} horas laboradas es:,'
      f' ${salario_bruto:,}\n')
print(f'El descuento salarial del profesor es: ${descuento:,}\n')
print(f'El salario neto (con descuento) del profesor por {horas} horas '
      f'laboradas es: ${salario_neto:,}\n')

# 9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.

print('\n--------- DATOS DEL ALQUILER DE TARJETAS DE LLAMADA ---------\n')
monto_inicial = float(input('Digite monto inicial de la tarjeta: '))
monto_final = float(input('Digite monto final de la tarjeta: '))

consumo_tarjeta = monto_inicial - monto_final
recargo_consumo = consumo_tarjeta * 0.2
costo_total = consumo_tarjeta + recargo_consumo

print('\n-------------- RESUMEN DEL COSTO DE LA LLAMADA  --------------\n')
print(f'Valor consumido de la tarjeta: ${consumo_tarjeta:,}\n')
print(f'Valor del recargo del 20%: ${recargo_consumo:,}\n')
print(f'Total costo de la llamada (consumo + recargo): ${costo_total:,}\n')

# 10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un algoritmo que determine el monto a pagar por un
# revelado completo sabiendo que adiconalmente le cobran el IVA
# (16%).

print('\n--------- DATOS DEL REVELADO DE ROLLOS  ---------\n')
num_rollos = int(input('Digite número de rollos revelados: '))
costo_rollos = num_rollos * 1500
iva = costo_rollos * 0.16
costo_total = costo_rollos + iva

print('\n----------- RESUMEN DEL COSTO DE REVELADO DE ROLLOS -----------\n')
print(f'Costo de revelado de {num_rollos} rollos: ${costo_rollos:,}\n')
print(f'Costo del Iva del 16%: ${iva:,}\n')
print(f'Costo total del revelado de rollos (costo + Iva): ${costo_total:,}\n')

# 11. . En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte
# conforme a la siguiente tabla:

"""
--------------------------------------------
|      AREA       | Porcentaje presupuestal |
--------------------------------------------
|  Ginecología    |          40%            |
--------------------------------------------
|  Traumatología  |          30%            |
--------------------------------------------
|  Pediatría      |          30%            |
--------------------------------------------
"""

# Obtener la cantidad de dinero que recibirá cada área, para cualquier
# monto presupuestal.

print('\n----- DATOS PARA EL CÁLCULO PRESUPUESTAL HOSPITALARIO  ---------\n')
monto_presupuesto = float(input('Digite monto presupuestal: '))
ginecologia = monto_presupuesto * 0.4
Traumatologia = monto_presupuesto * 0.3
pediatria = monto_presupuesto * 0.3

print('\n----------- RESUMEN PRESUPUESTAL DEL HOSPITAL -----------\n')
print(f'Monto presupuestal hospitalario: ${monto_presupuesto:,}\n')
print(f'Monto presupuestal asignado a ginecología: ${ginecologia:,}\n')
print(f'Monto presupuestal asignado a Traumatología: ${Traumatologia:,}\n')
print(f'Monto presupuestal asignado a Pediatría: ${pediatria:,}\n')

# 12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# algoritmo que teniendo como dato de entrada el total de películas
# alquiladas, y el número de días de alquiler, determine el monto a
# pagar.

print('\n----- DATOS PARA EL CÁLCULO DEL ALQUILER DE DVD ---------\n')
num_dvd = int(input('Digite cantidad de DVD alquilados: '))
dias = int(input('Digite la cantidad de días de alquiler: '))
valor_alquiler = (num_dvd - 1) * dias * 1500

print('\n----------- RESUMEN VALOR DE ALQUILER DE DVD -----------\n')
print(f'La cantidad total de DVD alquilados es {num_dvd}, uno de estos es '
      f'gratis, por lo que se cobra el equivalente a {num_dvd-1} DVDs \n')
print(f'El valor del alquiler de los {num_dvd} DVDs por {dias} días '
      f'es: ${valor_alquiler:,}\n')

# 13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un algoritmo que determine el monto a
# pagar por una familia que desee realizar dicho Tour sabiendo que
# también cobran el 12% de IVA.

print('\n----- DATOS PARA LA COTIZACIÓN DE TOUR POR CARTAGENA ---------\n')
num_personas = int(input('Digite cantidad de personas: '))
dias = int(input('Digite cantidad de días para el tour: '))
costo_tour = num_personas * dias * 25000
iva = costo_tour * 0.12
costo_total = costo_tour + iva

print('\n--------- RESUMEN DE COTIZACIÓN DE TOUR EN CARTAGENA ---------\n')
print(f'El costo antes de Iva por {dias} días para una familia de '
      f'{num_personas} personas es: ${costo_tour:,}\n')
print(f'Costo del Iva del 12%: ${iva:,}\n')
print(f'Costo total del tour es (costo + Iva): ${costo_total:,}\n')







