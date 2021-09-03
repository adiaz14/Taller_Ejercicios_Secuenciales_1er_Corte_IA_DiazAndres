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
