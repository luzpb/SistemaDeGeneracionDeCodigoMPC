# Importar paquetes.
import cvxpy as cp
import numpy as np

# Definir los datos del problema de forma directa.
Q = np.array({{ Q }})
c = np.array({{ c }})
n = {{ n }}

m = {{ m }}  # Número de restricciones lineales afines
A = np.array({{ A }})  # Matriz A
b = np.array({{ b }})  # Vector b

# Definir y resolver el problema CVXPY con los datos definidos.
x = cp.Variable(n)
objective = (1/2) * cp.quad_form(x, Q) + c.T @ x

constraints = [A @ x == b]

prob = cp.Problem(cp.Minimize(objective), constraints)
prob.solve()

# Imprimir el resultado.
print("Estado de resolución:", prob.status)
print("Valor óptimo de la función objetivo:", prob.value)
print("Valores de las variables de decisión:")
for i, value in enumerate(x.value):
    print("x[{}]: {}".format(i, value))