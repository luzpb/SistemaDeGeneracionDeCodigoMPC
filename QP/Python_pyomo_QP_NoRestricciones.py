
from pyomo.environ import ConcreteModel,Var,Objective, minimize,SolverFactory

# Código Python_pyomo_QP_R.py

# Definir los datos del problema
n = {{ n }}  # Dimensión del problema

Q = {{ Q }}  # Matriz Q
c = {{ c }}  # Vector c

# Crear una instancia del modelo de optimización
model = ConcreteModel()

# Definir las variables de decisión
model.x = Var(range(n), bounds=(-float('inf'), float('inf')))  # Añadir límites a las variables

# Definir la función objetivo
model.objective = Objective(
    expr=0.5 * sum(Q[i][j] * model.x[i] * model.x[j] for i in range(n) for j in range(n))
    + sum(c[i] * model.x[i] for i in range(n)),
    sense=minimize
)

# Resolver el problema de optimización
solver = SolverFactory('ipopt')
solver.options['max_iter'] = 1000  # Aumentar el número máximo de iteraciones
result = solver.solve(model)

# Imprimir el resultado
print("Objective value:", model.objective())
print("Decision variables:")
for i in range(n):
    print("x[{}]: {}".format(i, model.x[i]()))