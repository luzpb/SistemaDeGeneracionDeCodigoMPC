from pyomo.environ import minimize, inequality, ConcreteModel, Var, Constraint, RangeSet, Objective, SolverFactory
import numpy as np

# Crear un modelo de Pyomo
model = ConcreteModel()

# Parámetros
N ={{N}} # Horizonte de predicción

# Matrices del sistema
A = np.array({{A}})  # Matriz de estado
B = np.array({{B}})  # Matriz de entrada
nx, nu = B.shape  # nx: Dimensionalidad del estado nu:Dimensionalidad de la entrada de control

# Estado inicial del sistema
x0 = {{x0}} 

# Matrices de ponderación
P = np.array({{P}})   # Matriz de ponderación para los estados en el costo del MPC
Q = np.array({{Q}}) # Matriz de ponderación para los estados en el costo del MPC
R = np.array({{R}})  # Matriz de ponderación para las entradas en el costo del MPC

# Límites de las variables de estado y control
xmin = np.array({{xmin}})  # Límite mínimo para las variables de estado
xmax = np.array({{xmax}})   # Límite máximo para las variables de estado
umin = {{umin}}        # Límite mínimo para la variable de control
umax = {{umax}}      # Límite máximo para la variable de control

# Conjunto de puntos de tiempo
model.t = RangeSet(0, N-1)

# Variables de estado y control
model.x = Var(range(nx), model.t)
model.u = Var(range(nu), model.t)

# Ecuaciones de estado
def state_eqs_rule(model, i, t):
    if t == 0:
        return model.x[i, t] == x0[i]
    return model.x[i, t] == sum(A[i, j] * model.x[j, t-1] for j in range(nx)) + B[i, 0] * model.u[0, t-1]

model.state_eqs = Constraint(range(nx), model.t, rule=state_eqs_rule)

# Límites de las variables de estado
def state_limits_rule(model, i, t):
    return inequality(xmin[i, 0], model.x[i, t], xmax[i, 0])

model.state_limits = Constraint(range(nx), model.t, rule=state_limits_rule)

# Límites de la variable de control
def control_limits_rule(model, t):
    return inequality(umin, model.u[0, t], umax)

model.control_limits = Constraint(model.t, rule=control_limits_rule)

# Función de costo
def cost_rule(model):
    cost = 0
    for t in model.t:
        cost += sum((model.x[i, t]) * P[i, j] * (model.x[j, t]) for i in range(nx) for j in range(nx))
        cost += (model.u[0, t]) * R[0, 0] * (model.u[0, t])
    return cost

model.cost = Objective(rule=cost_rule, sense=minimize)

# Resolver el problema de optimización
solver = SolverFactory('gurobi')
results = solver.solve(model)

# Extraer los resultados
x_opt = np.array([[model.x[i, t]() for t in model.t] for i in range(nx)])
u_opt = np.array([model.u[0, t]() for t in model.t])

# Imprimir resultados
print("Estado óptimo:")
print(x_opt)
print("Control óptimo:")
print(u_opt)
