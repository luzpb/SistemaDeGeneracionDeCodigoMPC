import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
import time

start_time = time.time() 

N = 20
alpha = 1.5  

# Matrices del sistema
A = np.array([[0.9, 0.5], [-0.2, 0.8]])
B = np.array([[1.0], [0.5]])
[nx, nu] = B.shape

x_0 = np.array([3.0, 3.0])  # Inicialización corregida de x_0 como un vector columna

x = cp.Variable((nx, N + 1))
u = cp.Variable((nu, N))

P = alpha * np.eye(nx)
Q = np.eye(nx)  # Definición de la matriz Q
R = np.eye(nu)  # Definición de la matriz R


# Definir función de costo
def cost_function(x, u):
    x_cost = cp.sum_squares(Q @ x[:, :-1])  # Costo de estados excepto el último
    u_cost = cp.sum_squares(R @ u)  # Costo de acciones de control
    final_x_cost = cp.sum_squares(P @ x[:, -1])  # Costo del estado final
    return x_cost + u_cost + final_x_cost

# Implementar el algoritmo del MPC
x_result = [x_0]
u_result = []

for _ in range(20):  # Reducimos las iteraciones a 20
    
    constraints = []  # Restricciones en cada iteración
    for t in range(N):
        constraints += [x[:, t + 1] == A @ x[:, t] + B @ u[:, t]]

    # Restricción de condición inicial en la primera iteración
    if x_result[-1] is not None:
        constraints += [x[:, 0] == x_result[-1]]
    
    # Definir el problema de optimización en cada iteración
    objective = cp.Minimize(cost_function(x, u))
    problem = cp.Problem(objective, constraints)

    # Resolver el problema de optimización para obtener la acción de control óptima
    problem.solve(solver=cp.GUROBI, verbose=False)

    # Obtener la acción de control óptima y almacenarla
    u_k = u[:, 0].value
    u_result.append(u_k)

    # Aplicar la primera acción de control al sistema y avanzar en el tiempo
    x_k1 = A @ x_result[-1] + B @ u_k
    x_result.append(x_k1)
    print(f"x: {x_result[-1]}, u: {u_k}")
    
end_time = time.time()  # Tomar el tiempo de finalización
execution_time = end_time - start_time

print(f"\n Tiempo de ejecución: {execution_time:.6f} segundos")
    
# Convertir las listas en arrays para facilitar el plot
x_result = np.array(x_result)
u_result = np.array(u_result)

# Plot de las variables de estado
plt.figure()
plt.plot(x_result[:, 0], label='x1')
plt.plot(x_result[:, 1], label='x2')
plt.xlabel('Tiempo')
plt.ylabel('Variables de Estado')
plt.legend()
plt.grid(True)

# Plot de las acciones de control
plt.figure()
plt.plot(u_result[:, 0], label='u')
plt.xlabel('Tiempo')
plt.ylabel('Acción de Control')
plt.legend()
plt.grid(True)

# Mostrar los plots
plt.show()
