'''En caso de SyntaxError: invalid syntax, asegurate de que las variables no completadas sean = None'''

"""
VARIABLES PARA PROBLEMA CUADRATICO (QP)

        min⁡        ⁡〖1/2〗 x^T Qx + c^Tx  
        suj.a:      Ax = b 
                    Gx ≤ h
"""
# # Dimensión del problema
# n = 3

# # Matriz Q
# Q = [
#     [1.0, 0.0, 0.0],
#     [0.0, 2.0, 0.0],
#     [0.0, 0.0, 3.0]]

# # Vector c
# c = [1.0, 2.0, 3.0]

# # Puedes agregar más variables y datos según tus necesidades

# # Por ejemplo:
# # Restricciones de desigualdad
# p = 2
# G = [ [1.0, 0.0, 0.0],
#     [0.0, 1.0, 0.0]]
# h = [0.5, 1.0]

# # Restricciones lineales
# m = 1
# A = [[1.0, 1.0, 1.0]]
# b = [1.0]

"""
VARIABLES PARA PROBLEMA MPC

""" 

import numpy as np 
# Matrices del sistema
A =[[ 0.9,  0.5],
       [-0.2,  0.8]]  # Matriz de estado
B = [[1. ],
       [0.5]] # Matriz de entrada

# Horizonte de predicción y control
N = 5

# Límites del estado y control
xmin = [[-5], [-5]]
xmax = [[5], [10]]
umin = -2
umax = 2

x0 = [[-1.],
       [-2.]] # Inicialización corregida de x_0 como un vector columna

P = [[4., 0.],
       [0., 4.]]
Q = [[4., 0.],
       [0., 4.]] 
R = [[3.]]  # Definición de la matriz R

# Definición de referencias para el estado en cada paso de tiempo
uref=[[0.0], [0.0], [0.0],[0.0],[0.0]]
xref=[[0.0, 0.0], [1.0, 0.5], [0.5, 1.0], [0.2, 0.8], [0.0, 0.0], [0.0, 0.0]]

