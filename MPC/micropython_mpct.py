import numpy as np
import scipy
import cvxopt
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


# Definición de referencias para el estado en cada paso de tiempo
xref = [np.array(item) for item in {{ xref}}]
uref = [np.array(item) for item in {{ uref}}]

# Ponderaciones de costo para el MPC (personalizables)
Q = np.array({{Q}})   # Matriz de ponderación para los estados en el costo del MPC
R = np.array({{R}})   # Matriz de ponderación para las entradas en el costo del MPC
P = np.array({{P}}) # Matriz de ponderación terminal para los estados en el costo del MPC

# Estado inicial del sistema
x0 =np.array({{x0}})  # Inicialización corregida de x_0 como un vector columna


# Ponderaciones de costo para las variables de control 'u' y variables de estado 'x'
m = N * nu + N * nx

# Combinar las ponderaciones para formar la matriz Hessiana 'H'
H =2* scipy.linalg.block_diag(np.kron(np.eye(N), R), np.kron(np.eye(N), Q))
# Vector de referencia para las variables de control 'u' y variables de estado 'x'

c = np.zeros(N * (nu + nx))  # Inicializar un array de ceros de la longitud necesaria

for t in range(N):
    c_u_t = -2 * R @ np.array(uref[t])  # Convertir uref[t] en un array de NumPy
    c[t * nu: (t + 1) * nu] = c_u_t.flatten()  # Asignar los valores de c_u_t a la parte correspondiente de c

    c_x_t = -2 * Q @ np.array(xref[t])  # Convertir xref[t] en un array de NumPy
    c[N * nu + t * nx: N * nu + (t + 1) * nx] = c_x_t.flatten()  # Asignar los valores de c_x_t a la parte correspondiente de c
 
# Matriz de restricciones de desigualdad
G = np.block([np.eye(N * nu), np.zeros((N * nu, N * nx))])

# Matriz de restricciones de igualdad (se llenará más adelante)
Aeq = np.zeros((N * nx, m))

for i in range(N):
    Aeq[i * nx: (i + 1) * nx, i * nu: (i + 1) * nu] = -B
    Aeq[i * nx: (i + 1) * nx, N * nu + i * nx: N * nu + (i + 1) * nx] = np.eye(nx)

# Rellenar con -A a la izquierda de I_{nx} a partir de la fila N y nx columnas hacia la izquierda
for i in range(N-1):
    Aeq[i * nx + nx: (i + 1) * nx + nx, N * nu + i * nx : N * nu + (i + 1) * nx] = -A
  

# Agregamos la matriz A' a la primera parte de beq
beq = np.vstack((A, np.zeros(((N - 1) * nx, nx)))) @ x0

G = np.zeros((0, (nx + nu) * N))
h = np.zeros((0, 1))
if umax is not None:
    
    tG = np.hstack([np.eye(N * nu), np.zeros((N * nu, nx * N))])
    th = np.kron(np.ones((N * nu, 1)), umax)
    G = np.vstack([G, tG])
    h = np.vstack([h, th])

if umin is not None:
    tG = np.hstack([np.eye(N * nu) * -1.0, np.zeros((N * nu, nx * N))])
    th = np.kron(np.ones((N, 1)), umin * -1.0)
    G = np.vstack([G, tG])
    h = np.vstack([h, th])

if xmax is not None:
    tG = np.hstack([np.zeros((N * nx, nu * N)), np.eye(N * nx)])
    th = np.kron(np.ones((N, 1)), xmax)
    G = np.vstack([G, tG])
    h = np.vstack([h, th])

if xmin is not None:
    tG = np.hstack([np.zeros((N * nx, nu * N)), np.eye(N * nx) * -1.0])
    th = np.kron(np.ones((N, 1)), xmin * -1.0)
    G = np.vstack([G, tG])
    h = np.vstack([h, th])

# Exportar las matrices a un archivo separado 
# Escribir las matrices en un archivo .txt
with open("mpc_qp_matrices.py", "w") as file:
    file.write("H = " + str(H.tolist()) + "\n")
    file.write("c = " + str(c.tolist()) + "\n")
    file.write("G = " + str(G.tolist()) + "\n")
    file.write("h = " + str(h.tolist()) + "\n")
    file.write("A_eq = " + str(Aeq.tolist()) + "\n")
    file.write("b_eq = " + str(beq.tolist()) + "\n")

# Resolver el problema de programación cuadrática (Convertir matrices numpy a matrices CVXOPT)
sol = cvxopt.solvers.qp(P=cvxopt.matrix(H) , q=cvxopt.matrix(c), G=cvxopt.matrix(G), h=cvxopt.matrix(h), A=cvxopt.matrix(Aeq), b=cvxopt.matrix(beq))

# Extraer los estados y controles óptimos
u_opt = np.array(sol['x'][:N * nu])
x_opt = np.array(sol['x'][N * nu:])

# Reorganizar los estados y controles para que estén en el formato correcto
u_opt = u_opt.reshape((N, nu)).T
x_opt = x_opt.reshape((N, nx)).T

end_time = time.time()

# Impresión de los resultados
print("\nTiempo de ejecución de transform_mpc_to_qp:", end_time, "segundos")

# Impresión de los resultados
print("\nEstados y Controles Óptimos:")
for t in range(N):
    print(f"Paso de tiempo {t+1}: x = {x_opt[:, t]}, u = {u_opt[:, t]}")
 