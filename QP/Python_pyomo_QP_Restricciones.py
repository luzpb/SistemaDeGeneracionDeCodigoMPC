from pyomo.environ import ConcreteModel,Var,Objective,ConstraintList, minimize,SolverFactory

# Definir los datos del problema
n = {{ n }}  # Dimensión del problema

Q = {{ Q }}  # Matriz Q
c = {{ c }}  # Vector c
m = {{ m }}  # Número de restricciones lineales afines
A = {{ A }}  # Matriz A
b = {{ b }}  # Vector b
p = {{ p }}  # Número de restricciones de desigualdad
G = {{ G }}  # Matriz G
h = {{ h }}  # Vector h

# Crear una instancia del modelo de optimización
model = ConcreteModel()

# Definir las variables de decisión
model.x = Var(range(n))

# Definir la función objetivo
model.objective = Objective(
    expr=0.5 * sum(Q[i][j] * model.x[i] * model.x[j] for i in range(n) for j in range(n))
          + sum(c[i] * model.x[i] for i in range(n)),
    sense=minimize
)

# Definir las restricciones de igualdad
model.equality_constraints = ConstraintList()
for i in range(m):
    model.equality_constraints.add(
        sum(A[i][j] * model.x[j] for j in range(n)) == b[i]
    )

# Definir las restricciones de desigualdad
model.inequality_constraints = ConstraintList()
for i in range(p):
    model.inequality_constraints.add(
        sum(G[i][j] * model.x[j] for j in range(n)) <= h[i]
    )

# Resolver el problema de optimización
solver = SolverFactory('gurobi')
result = solver.solve(model, tee=False)

# Imprimir el resultado
print("Objective value:", model.objective())
print("Decision variables:")
for i in range(n):
    print("x[{}]: {}".format(i, model.x[i]()))
