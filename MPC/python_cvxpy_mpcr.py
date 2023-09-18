import numpy as np
import cvxpy as cp
import time

start_time = time.time() 

# Matrices del sistema
A = np.array({{A}})  # Matriz de estado
B = np.array({{B}})  # Matriz de entrada

# Dimensiones de los estados (nx) y las entradas (nu)
[nx, nu] = B.shape

# Horizonte de predicción y control
N ={{N}}

# Límites del estado y control
xmin = np.array({{xmin}})
xmax = np.array({{xmax}})
umin = {{umin}}
umax = {{umax}}

# Ponderaciones de costo para el MPC (personalizables)
Q = np.array({{Q}})   # Matriz de ponderación para los estados en el costo del MPC
R = np.array({{R}})   # Matriz de ponderación para las entradas en el costo del MPC
P = np.array({{P}}) # Matriz de ponderación terminal para los estados en el costo del MPC

# Estado inicial del sistema
x0 =np.array({{x0}})  # Inicialización corregida de x_0 como un vector columna

# Definición de las variables de estado y control para el MPC
x = cp.Variable((nx, N + 1))  # Variables de estado en cada paso de tiempo
u = cp.Variable((nu, N))  # Variables de control en cada paso de tiempo

# Inicialización del costo total y la lista de restricciones para el MPC
costlist = 0.0
constrlist = []

# Creación del problema de optimización para el MPC
for k in range(N):
    # Costo de control cuadrático en cada paso de tiempo
    costlist += cp.quad_form(x[:, k], Q)  # Penalize deviation from state reference
    costlist += cp.quad_form(u[:, k], R)  # Penalize deviation from control reference

    # Restricciones de evolución del sistema (dinámica)
    constrlist += [x[:, k + 1] == A @ x[:, k] + B @ u[:, k]]

    # Restricciones de límites para las entradas
    constrlist += [u <= umax]
    constrlist += [u >= umin]

# Costo terminal cuadrático en el último paso de tiempo
costlist += cp.quad_form(x[:, N], P)  # Penalize deviation from terminal state reference

# Restricción de estado inicial
constrlist += [x[:, 0] == x0[:, 0]]

# Creación y resolución del problema de optimización del MPC
prob = cp.Problem(cp.Minimize(costlist), constrlist)
prob.solve(solver=cp.GUROBI)

# Extracción de los valores óptimos de los estados y controles
x_opt = np.array([x[:, t].value for t in range(N+1)]).T
u_opt = np.array([u[:, t].value for t in range(N)]).T

end_time = time.time()

# Impresión de los resultados
print("Tiempo de ejecución de mpc_control:", end_time, "segundos")

# Impresión de los resultados
print("Estados y Controles Óptimos:")
for t in range(N):
    print(f"Paso de tiempo {t+1}: x = {x_opt[:, t+1].T}, u = {u_opt[:, t].T}")
