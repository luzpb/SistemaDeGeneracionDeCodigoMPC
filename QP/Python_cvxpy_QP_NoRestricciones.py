# Importar paquetes.
import cvxpy as cp
import numpy as np

Q = np.array({{ Q }})
c = np.array({{ c }})
n = {{ n }}

# Definir y resolver el problema CVXPY sin restricciones.
x = cp.Variable(n)
objective = (1/2) * cp.quad_form(x, Q) + c.T @ x
prob = cp.Problem(cp.Minimize(objective))

prob.solve()

# Imprimir el resultado.
print("Estado de resolución:", prob.status)
print("Valor óptimo de la función objetivo:", prob.value)
print("Valores de las variables de decisión:")
for i, value in enumerate(x.value):
    print("x[{}]: {}".format(i, value))