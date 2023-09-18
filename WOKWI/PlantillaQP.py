import math
import random
from ulab import numpy as np

# Parámetros del problema
H = np.array([[2.0, 1.0], [1.0, 2.0]])
q = np.array([1.0, 1.0])
A_eq = np.array([[1.0, 1.0]])
b = np.array([1.0])
G = np.array([[-1.0, 0.0], [0.0, -1.0]])
h = np.array([0.0, 0.0])

# Parámetros del algoritmo
learning_rate = 0.1
iterations = 1000
convergence_threshold = 1e-6

# Función objetivo
def objective_function(z):
    return 0.5 * np.sum(z @ (H @ z)) + q @ z

# Gradiente de la función objetivo
def gradient(z):
    return H @ z + q

# Proyección sobre restricciones lineales
def project(z):
    dot_products = G @ z
    violation_indices = np.where(dot_products > h)[0]
    z -= learning_rate * np.sum(G[violation_indices], axis=0)
    return z

# Inicialización aleatoria de la solución
z = np.array([random.uniform(0, 1) for _ in range(len(q))])

# Algoritmo de descenso del gradiente proyectado
for _ in range(iterations):
    grad = gradient(z)
    z_new = z - learning_rate * grad
    z_new = project(z_new)
    
    # Condición de parada basada en la diferencia de soluciones
    if np.sum((z_new - z)**2) < convergence_threshold:
        break
    
    z = z_new

# Imprimir la solución
print("Solución aproximada:", z)
print("Valor objetivo:", objective_function(z))
