from ulab import numpy as np
import Matrices
import utime  # Importar el módulo de tiempo

# Medir el tiempo de ejecución inicial
start_time = utime.ticks_ms()

H = np.array(Matrices.H)
c = np.array(Matrices.c)
A_eq = np.array(Matrices.A_eq)
b_eq = np.array(Matrices.b_eq)
G = np.array(Matrices.G)  
h = np.array(Matrices.h)  

# Definir la función objetivo, su gradiente y la proyección en el gradiente
def objective_function(x):
    return 0.5 * np.dot(np.dot(x.transpose(), H), x) + np.dot(c.transpose(), x) + np.dot(h.transpose(), np.maximum(0, np.dot(G, x) - h))


def gradient(x):
    return np.dot(H, x) + c

def project_to_equality_constraints(x):
    A_eq_transpose = A_eq.transpose()
    A_eq_inverse = np.linalg.inv(np.dot(A_eq, A_eq_transpose))
    x = x - np.dot(np.dot(A_eq_transpose, A_eq_inverse), np.dot(A_eq, x) - b_eq)
    return x

# Parámetros y configuración
learning_rate = 0.1
num_iterations = 100
initial_guess = 0*c

x = initial_guess

# Medir el tiempo de ejecución inicial
start_time = utime.ticks_ms()

# Descenso de gradiente con proyección en el gradiente para restricciones de igualdad
for _ in range(num_iterations):
    grad = gradient(x)
    x = x - learning_rate * grad
    x = project_to_equality_constraints(x)

# Medir el tiempo de ejecución final
end_time = utime.ticks_ms()
execution_time_ms = utime.ticks_diff(end_time, start_time)

# Resultado
optimal_solution = x

print("Solución óptima:", optimal_solution)
print("Tiempo de ejecución:", execution_time_ms, "milisegundos")
